# Generated by Django 4.2.6 on 2023-10-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_user_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user_creator',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='создатель'),
        ),
    ]
