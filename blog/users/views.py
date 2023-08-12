from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UsersAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def put(self,request):
        username = request.data.get('username')
        user = User.objects.filter(username = username).first()
        serializer = UserSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.update()
            return Response( {"message" : "User Successfully Updated"},status=201)

        return Response(serializer.errors, status=400)

