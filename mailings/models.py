from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.TextField(verbose_name='тескт сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailings(models.Model):
    day = 'D'
    week = 'W'
    month = 'M'
    periodicity_choises = [
        (day, 'day'),
        (week, 'week'),
        (month, 'month'),
    ]
    name = models.CharField(default='Рассылка', max_length=150, verbose_name='название рассылки')
    periodicity = models.CharField(
        max_length=1,
        choices=periodicity_choises,
        default=day,
    )
    completed = 'COM'
    created = 'CRE'
    launched = 'LAU'

    status_choises = [
        (completed, 'completed'),
        (created, 'created'),
        (launched, 'launched'),
    ]
    status = models.CharField(verbose_name='статус рассылки',
                              max_length=3,
                              choices=status_choises,
                              default=created,
                              )
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
