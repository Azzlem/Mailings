from django.db import models

from default import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    img = models.ImageField(upload_to='blog/', verbose_name='изображение')
    number_of_views = models.IntegerField(verbose_name='количество просмотров')
    date_of_published = models.DateField(verbose_name='дата публикации')
    user_created = models.EmailField(verbose_name='создатель', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.number_of_views} {self.date_of_published}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блогы'
