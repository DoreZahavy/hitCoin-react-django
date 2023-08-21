from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import AppUser, Move
from django.db.models import Q
from rest_framework.response import Response
from .serializers import AppUserSerializer, MoveSerializer

class UserListView(generics.ListAPIView):
    # queryset = Contact.objects.all()
    # serializer_class = ContactSerializer
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

class UserDetailView(generics.RetrieveAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    def retrieve(self, request, pk, *args, **kwargs):
        user = self.get_object()
        user_serializer = AppUserSerializer(user)

        user_id =pk
        print(user_id)
        moves = Move.objects.filter(Q(from_user_id=user_id) | Q(to_user_id=user_id))
        moves_serializer = MoveSerializer(moves, many=True) 
        response_data = {
            **user_serializer.data,
            'moves': moves_serializer.data

        }
        return Response(response_data)

        

class UserCreateView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

class UserDeleteView(generics.DestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
