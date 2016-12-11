from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Переопределяем пользователя, добавляем аватарку и покупки
    """
    avatar = models.ImageField(null=True, verbose_name='Аватарка', upload_to='avatars')
    products = models.ManyToManyField('self', verbose_name='Покупки', symmetrical=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

