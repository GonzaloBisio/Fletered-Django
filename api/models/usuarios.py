from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    dni = models.CharField(max_length=20)
    firebase_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name} {self.surname}"