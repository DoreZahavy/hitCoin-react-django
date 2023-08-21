from django.db import models
from user.models import AppUser

# class Contact(models.Model):
#     from_user = models.ForeignKey(AppUser, related_name='from_contacts', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(AppUser, related_name='to_contacts', on_delete=models.CASCADE)
    

#     class Meta:
#         unique_together = ('from_user', 'to_user')
