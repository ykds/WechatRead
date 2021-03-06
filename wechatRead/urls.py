"""wechatRead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from .settings import MEDIA_ROOT, MEDIA_URL
from books.urls import route as b_route
#from users.urls import route as u_route

import xadmin

urlpatterns = [
    url('^xadmin/', xadmin.site.urls),
    url('^doc/', include_docs_urls(title='微信读书')),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(b_route.urls)),
    url(r'^login/', obtain_jwt_token),
    #url(r'^', include(u_route.urls)),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
