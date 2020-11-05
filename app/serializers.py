from django.contrib.auth.models import User
from app.models import Post, Category
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'posts']



class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False)
    category = CategorySerializer(required=False)
    
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        id_ = validated_data.pop('category')
        category = Category.objects.get(id=id_)
        validated_data['category'] = category
        return super(PostSerializer, self).create(validated_data)

