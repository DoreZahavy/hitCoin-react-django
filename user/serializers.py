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

# class MoveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Move
#         fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    to_user_name = serializers.ReadOnlyField(source='to_user.name')
    from_user_name = serializers.ReadOnlyField(source='from_user.name')

    class Meta:
        model = Move
        fields = ['id', 'from_user', 'from_user_name', 'to_user', 'to_user_name', 'coins', 'created']