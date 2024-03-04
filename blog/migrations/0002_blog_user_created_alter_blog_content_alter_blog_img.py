# Generated by Django 4.2.6 on 2023-10-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_created',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='создатель'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='содержимое'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='blog/', verbose_name='изображение'),
        ),
    ]
