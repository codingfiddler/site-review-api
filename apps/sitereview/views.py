from django.shortcuts import render
from rest_framework.views import APIView
from apps.sitereview.serializers import (
    UserSerializer, WebsiteSerializer, PageSerializer, CommentSerializer
)
from apps.sitereview.models import Website, Page, Comment
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class WebsiteViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteSerializer
    queryset = Website.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['website']

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'page']

