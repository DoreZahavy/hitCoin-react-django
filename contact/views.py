from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import AppUser

class AddContactView(APIView):
    def post(self, request, user_id, contact_id):
        print(user_id,contact_id)
        try:
            user = AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # contact_id = request.data.get('contact_id')
        if contact_id:
            try:
                contact = AppUser.objects.get(pk=contact_id)
                user.contacts.add(contact)
                return Response({'message': 'Contact added successfully.'})
            except AppUser.DoesNotExist:
                return Response({'error': 'Contact does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Contact ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

class RemoveContactView(APIView):
    def post(self, request, user_id, contact_id):
        
        try:
            user = AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # contact_id = request.data.get('contact_id')
        if contact_id:
            try:
                contact = AppUser.objects.get(pk=contact_id)
                user.contacts.remove(contact)
                return Response({'message': 'Contact removed successfully.'})
            except AppUser.DoesNotExist:
                return Response({'error': 'Contact does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Contact ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

class UserContactsView(APIView):
    def get(self, request, user_id):
        try:
            user = AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        contacts = user.contacts.all()
        mini_contacts = [{"id":contact.id,"name":contact.name,"phone":contact.phone,"email":contact.email} for contact in contacts]
        return Response( mini_contacts)


class UserContactDetailView(APIView):
    def get(self, request, user_id, contact_id):
        try:
            user = AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            contact = user.contacts.get(pk=contact_id)
            return Response({"id":contact.id,"name":contact.name,"phone":contact.phone,"email":contact.email})
        except AppUser.DoesNotExist:
            return Response({'error': 'Contact does not exist for this user.'}, status=status.HTTP_404_NOT_FOUND)