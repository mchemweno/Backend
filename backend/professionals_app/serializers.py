from djoser.serializers import UserCreateSerializer

from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'profile_picture', 'email', 'phone', 'first_name', 'last_name', 'bio', 'average_rating', 'user_type', 'service')


class CategorySerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Category
        fields = '__all_'


class ServiceSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Service
        fields = '__all__'
