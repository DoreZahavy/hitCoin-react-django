from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import AppUser
from .serializers import AppUserSerializer

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
