from django.db import models
from user.models import AppUser

# class Move(models.Model):
#     from_user = models.ForeignKey(AppUser, related_name='from_user', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(AppUser, related_name='to_user', on_delete=models.CASCADE)
#     coins = models.IntegerField(default=100)
#     created = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         unique_together = ('from_user', 'to_user')
