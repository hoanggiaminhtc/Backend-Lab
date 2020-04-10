from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from news.models import News,Comment



# Create your views here.
class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    lookup_field = 'id'

class NewsListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
#Comment API
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    lookup_field = 'id'

class CommentListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()
