from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
NULLABLE = {'blank':  True, 'null': True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []