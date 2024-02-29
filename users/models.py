from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Создаем кастомную модель пользователя, AbstractUser
class CustomUser(AbstractUser):
    filial = models.CharField(max_length=256, verbose_name='Филиал')
    root_dir_user = models.CharField(max_length=256, verbose_name='Корневая папка пользователя')
    is_personal = models.BooleanField(default=True, verbose_name='Персональная учетная запись')
