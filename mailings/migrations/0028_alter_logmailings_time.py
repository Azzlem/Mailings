# Generated by Django 4.2.6 on 2023-10-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0027_alter_logmailings_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmailings',
            name='time',
            field=models.CharField(blank=True, null=True, verbose_name='время рассылки'),
        ),
    ]
