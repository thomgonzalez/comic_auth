from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.actions import PerfileAction



class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'id', 
            'name', 
            'age',
        )
        
    def get_name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        
        return f'{first_name} {last_name}'
    
    def get_age(self, obj):
        perfil = PerfileAction()
        queryset = perfil.get(**{'user': obj})
        return queryset.age if queryset else None


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)