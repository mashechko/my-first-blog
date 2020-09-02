from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(verbose_name='E-mail')
    profileimg = models.ImageField(verbose_name='Фото профиля', null=True)
    isauthor = models.BooleanField(verbose_name='Автор', default=False)
