from rest_framework.routers import DefaultRouter

from . import views

route = DefaultRouter()
route.register(r'categorys', views.CategoryViewSet)
route.register(r'books', views.BookViewSet)
route.register(r'bookcase', views.CollectionBookViewSet)