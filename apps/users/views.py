from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .serializers import FollowedSerializer, FollowingSerializer, VerifyCodeSerializer, UserRegisterSerializer, \
    UserDetailSerializer, AccountSerializer, FollowSerializer
from .models import Follow, EmailVerifyCode, Account
from .permissions import IsOwnerOrReadOnly, ReadOnly, OwnerOnly
from utils.send_email import send_email
from .filters import FollowFilter

User = get_user_model()

# Create your views here.
class CustomerBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception:
            return None


class VerifyCodeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    queryset = EmailVerifyCode.objects.all()
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = send_email(email, 'register')
        #EmailVerifyCode.objects.filter(email=email).delete()

        return Response({
            'email': email,
            'code': code,
        }, status=status.HTTP_201_CREATED)


class FollowViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):

    queryset = Follow.objects.all()
    #serializer_class = FollowSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, )
    filter_class = FollowFilter

    def get_serializer_class(self):

        if self.request:
            if self.request.query_params.get('followed', 'null') != 'null':
                return FollowedSerializer
            elif self.request.query_params.get('following', 'null') != 'null':
                return FollowingSerializer
        return FollowSerializer

    def get_permissions(self):

        if self.action == 'create' or self.action == 'destroy':
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [IsAuthenticated(), ReadOnly()]


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, )
    #lookup_field = User.id

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        account = Account()
        account.user = User.objects.filter(email=serializer.data['email'])[0]
        account.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):

        if self.action == 'create':
            return UserRegisterSerializer
        else:
            return UserDetailSerializer

    def get_permissions(self):

        if self.action == 'create':
            return []
        else:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]

    def get_object(self):
        return self.request.user


class AccountViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, OwnerOnly)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def get_object(self):
        return Account.objects.get(user=self.request.user)