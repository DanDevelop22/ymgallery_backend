from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    """Serializador para el registro"""
    class Meta:
        model = User
        fields = ('id','name','email','password')
        extra_keywords = {
            'password':{
                'write_only': True,
                'style':{'input_style':'password'}
            }
        }     

    def create(self, validated_data):
        """Crear y devolver un nuevo usuario"""
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )

        return user