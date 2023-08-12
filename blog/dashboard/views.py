from django.shortcuts import render
from posts.models import Post
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class PostsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/posts.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': queryset})




