from django.contrib.postgres.fields import JSONField
from django.db import models

from default import NULLABLE
from users.models import User


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.TextField(verbose_name='тескт сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    second_name = models.CharField(max_length=50, verbose_name='фамилия')
    sur_name = models.CharField(max_length=50, verbose_name='отчество')
    email = models.EmailField(max_length=150, verbose_name='почта')
    comments = models.TextField(verbose_name='коментарии', **NULLABLE)

    def __str__(self):
        return f'{self.second_name} {self.first_name} {self.sur_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailings(models.Model):
    day = 'Раз в день'
    week = 'Раз в неделю'
    month = 'Раз в месяц'
    periodicity_choises = [
        (day, 'day'),
        (week, 'week'),
        (month, 'month'),
    ]
    name = models.CharField(default='Рассылка', max_length=150, verbose_name='название рассылки')
    user_creator = models.EmailField(verbose_name='создатель',
                                     **NULLABLE)  # ForeignKey(User, on_delete=models.CASCADE, default='1')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default='2')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    periodicity = models.CharField(
        max_length=15,
        choices=periodicity_choises,
        default=day,
    )
    completed = 'Запущена'
    created = 'Создана'
    launched = 'Законченна'

    status_choises = [
        (completed, 'completed'),
        (created, 'created'),
        (launched, 'launched'),
    ]
    status = models.CharField(verbose_name='статус рассылки',
                              max_length=15,
                              choices=status_choises,
                              default=created,
                              )

    def __str__(self):
        return f'{self.name} {self.user_creator}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class IntersectionMailingsClients(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mailings = models.ForeignKey(Mailings, on_delete=models.CASCADE)
