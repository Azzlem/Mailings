from django.contrib.auth.models import AbstractUser
from django.db import models

from default import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    fio = models.CharField(max_length=150, verbose_name='ФИО', **NULLABLE)
    about = models.TextField(verbose_name='коментарии', **NULLABLE)
    token = models.CharField(max_length=22, verbose_name='Token для верификации почты', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='верифицированна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
