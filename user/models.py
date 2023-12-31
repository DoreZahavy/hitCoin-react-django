from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
    def create_user(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError('Email required')
        if not password:
            raise ValueError('Password required')
        
        email=self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class AppUser(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email= models.EmailField(max_length=50,unique=True)
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    coins = models.IntegerField(default=100)
    # moves = models.ManyToManyField("self", through='Move', symmetrical=False, related_name='moves_related')
    contacts = models.ManyToManyField("self", through='Contact', symmetrical=False, related_name='contacts_related')


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    from_user = models.ForeignKey(AppUser, related_name='from_contacts', on_delete=models.CASCADE)
    to_user = models.ForeignKey(AppUser, related_name='to_contacts', on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('from_user', 'to_user')

class Move(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(AppUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(AppUser, related_name='to_user', on_delete=models.CASCADE)
    coins = models.IntegerField(default=100)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('from_user', 'to_user')
