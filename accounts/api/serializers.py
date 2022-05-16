from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_popularity')
    
    class Meta:
        model = User
        fields = ['id', 'name', ]
        
    def name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        
        name = f'{first_name} {last_name}'
        return name


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)