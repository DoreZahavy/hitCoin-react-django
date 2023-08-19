from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'name','phone', 'email', 'coins', 'moves', 'contacts', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        # 'id',