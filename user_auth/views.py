from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.sessions.models import Session
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import status
from user.models import AppUser
from user.serializers import AppUserSerializer

class UserSignupView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = AppUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(generics.DestroyAPIView):
    queryset = Session.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
