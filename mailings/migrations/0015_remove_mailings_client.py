# Generated by Django 4.2.6 on 2023-10-15 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0014_remove_mailings_client_mailings_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailings',
            name='client',
        ),
    ]
