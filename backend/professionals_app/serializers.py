from django.db.migrations import serializer
from djoser.serializers import UserCreateSerializer

from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'profile_picture', 'email', 'phone', 'first_name', 'last_name', 'bio')


class CategorySerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Category
        fields = ('id', 'category_name')


class ServiceSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Service
        fields = ('id', 'service_name')
