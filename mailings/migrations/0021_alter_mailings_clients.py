# Generated by Django 4.2.6 on 2023-10-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0020_alter_mailings_user_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailings',
            name='clients',
            field=models.ManyToManyField(to='mailings.client', verbose_name='клиенты'),
        ),
    ]
