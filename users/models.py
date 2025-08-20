from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .mixins import UserMixins

# Create your models here.
class CustomUser(AbstractBaseUser):
    class Meta:
        db_table = 'users'
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    objects = UserMixins()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
