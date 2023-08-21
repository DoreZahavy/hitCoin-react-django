from rest_framework import serializers
from .models import AppUser , Contact , Move

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'name','phone', 'email', 'coins',  'contacts', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        # 'id',

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'