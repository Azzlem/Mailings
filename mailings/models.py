from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.TextField(verbose_name='тескт сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
