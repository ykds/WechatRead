from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book, Category, CollectionBook, Chapter, BookMark
from .serializers import BookSerializer, CategorySerializer, CollectionBookSerializer, ChapterSerializer, BookMarkSerializer
from .filters import BookFilter, ChapterFilter, BookMarkFilter
from .permissions import IsOwnerOrReadOnly, IsPubOrHasPurchased

# Create your views here.


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
        获取所有类别
    retrieve：
        获取一个类别
    """
    queryset = Category.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
        获取所有公共图书
    retrieve:
        获取单一本公共图书
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_class = BookFilter
    search_fields = ('$name',)


class CollectionBookViewSet(viewsets.ModelViewSet):

    queryset = CollectionBook.objects.all()
    serializer_class = CollectionBookSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ChapterViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
        获取所有章节
    retrieve:
        获取其中一个章节
    """

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = ChapterFilter
    permission_classes = (IsPubOrHasPurchased, )


class BookMarkViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    """
    create:
        增加书签
    list:
        获取所有书签
    retrieve:
        获取某一个书签
    destroy:
        删除一个书签
    """

    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BookMarkFilter