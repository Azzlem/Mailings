# Generated by Django 4.2.6 on 2023-10-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0026_logmailings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logmailings',
            options={'verbose_name': 'лог', 'verbose_name_plural': 'логи'},
        ),
    ]
