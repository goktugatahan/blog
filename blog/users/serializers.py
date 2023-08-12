from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(min_length = 8, required = False)
    email = serializers.CharField(required = True)

    def validate_email(self,email):
        return email

    def validate_username(self, username):
        return username

    def update(self):
        self.instance.username = self.validated_data.get("username", self.instance.username)
        self.instance.email = self.validated_data.get("email",self.instance.email)
        self.instance.save()
        return True

    class Meta:
        model = User
        fields = ('username','email','password', 'id')

