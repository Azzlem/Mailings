# Generated by Django 4.2.6 on 2023-10-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0018_alter_mailings_user_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailings',
            name='user_creator',
            field=models.EmailField(max_length=254, verbose_name='создатель'),
        ),
    ]
