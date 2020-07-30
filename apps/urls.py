"""sitereview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from apps.sitereview.views import UserViewSet, WebsiteViewSet, PageViewSet, CommentViewSet
from django.contrib.auth import authenticate, login
from apps.sitereview.views import UpView

urlpatterns = [
    url(r'^$', UpView.as_view(), name='up'),
    path('admin/', admin.site.urls),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(
        r'^users/(?P<pk>[0-9-]+)/$',
        UserViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
        }),
        name="user-single"
    ),
    path('websites/', WebsiteViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(
        r'^websites/(?P<pk>[0-9-]+)/$',
        WebsiteViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
        }),
        name="website-single"
    ),
    path('pages/', PageViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(
        r'^pages/(?P<pk>[0-9-]+)/$',
        PageViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
        }),
        name="page-single"
    ),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(
        r'^comments/(?P<pk>[0-9-]+)/$',
        CommentViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
        }),
        name="comment-single"
    ),
]
