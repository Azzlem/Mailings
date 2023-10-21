from django.db import models

from default import NULLABLE
from users.models import User


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    second_name = models.CharField(max_length=50, verbose_name='фамилия')
    sur_name = models.CharField(max_length=50, verbose_name='отчество')
    email = models.EmailField(max_length=150, verbose_name='почта', unique=True)
    comments = models.TextField(verbose_name='коментарии', **NULLABLE)
    user_creator = models.EmailField(verbose_name='создатель', **NULLABLE)

    def __str__(self):
        return f'{self.second_name} {self.first_name} {self.sur_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

