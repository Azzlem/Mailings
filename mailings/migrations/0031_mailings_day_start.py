# Generated by Django 4.2.6 on 2023-10-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0030_logmailings_user_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailings',
            name='day_start',
            field=models.DateField(blank=True, null=True, verbose_name='дата начала рассылки'),
        ),
    ]
