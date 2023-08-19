from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.sessions.models import Session
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import status
from user.models import AppUser
from user.serializers import AppUserSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LogoutView


class UserSignupView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # Hash the password before saving
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password

        return super().create(request, *args, **kwargs)

class UserLoginView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = AppUser.objects.filter(email=email).first()
        print(user)
        if user and user.check_password(password):
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(LogoutView):
    def logout(self, request, *args, **kwargs):
        print(request)  # Print the request.META dictionary
        return super().logout(request, *args, **kwargs)

    # pass
# class UserLogoutView(generics.DestroyAPIView):
#     # queryset = Session.objects.all()
#     print('before permission')
#     permission_classes = [permissions.IsAuthenticated]
#     print('after permission')

#     def destroy(self, request, *args, **kwargs):
#         logout(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)
