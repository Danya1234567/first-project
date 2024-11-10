from django.contrib.auth.models import AbstractUser
from django.db import models as m

# Create your models here.

class User(AbstractUser):
    surname = m.CharField(max_length=50)
    name = m.CharField(max_length=50)
    email = m.EmailField(max_length=100,null=True, blank=True)
    password = m.CharField(max_length=100)
    date_of_birth = m.DateField(null=True, blank=True)
    avatar = m.ImageField(upload_to='media/avatars', default='avatars/icon.png')
    role = [('admin', 'Admin'), ('arendator', 'arendator'), ('buyer', 'buyer'),('user', 'user')]
    role = m.CharField(max_length=10, choices=role, default='user')
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.surname} {self.name}"