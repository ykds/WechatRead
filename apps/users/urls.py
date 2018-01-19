from rest_framework.routers import DefaultRouter

from . import views


route = DefaultRouter()
route.register(r'code', views.VerifyCodeViewSet)
route.register(r'users', views.UserViewSet)
route.register(r'follow', views.FollowViewSet)
route.register(r'account', views.AccountViewSet)