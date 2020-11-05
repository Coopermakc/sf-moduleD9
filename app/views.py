from django.shortcuts import render
from app.models import Post, Category
from app.serializers import PostSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import generics, status


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def create(self, request):

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all().filter()
    serializer_class = CategorySerializer