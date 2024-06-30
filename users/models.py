from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=12, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

