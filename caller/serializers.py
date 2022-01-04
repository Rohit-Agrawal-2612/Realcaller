from django.db import models
from rest_framework import serializers
from caller.models import MyUser, UnauthUsers
from django.contrib.auth.hashers import make_password

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = ['is_admin','last_login','is_active','id',]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = MyUser.objects.create(**validated_data)
        user.password = make_password(user.password)
        user.save()
        return user

class UnauthUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnauthUsers
        exclude = ['id',]

