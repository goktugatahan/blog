from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework.response import Response
from .models import Post
from rest_framework.generics import get_object_or_404
from .serializers import PostsSerializer, PostSerializer
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.models import User

class PostsAPIView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts,many = True)
        return Response(serializer.data)

    def post(self,request):
        request.data['author'] = User.objects.filter(id = 1).first()
        serializer = PostsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class PostAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.filter(id=pk)
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data)

    def delete(self, request):
        post_id = request.data.get("post_id", None)
        post = Post.objects.filter(pk=post_id)
        post.delete()
        return Response(status=200)
