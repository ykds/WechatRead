from rest_framework.routers import DefaultRouter

from . import views


route = DefaultRouter()
route.register(r'code', views.VerifyCodeViewSet)