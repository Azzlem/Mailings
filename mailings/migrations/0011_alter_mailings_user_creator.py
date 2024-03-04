# Generated by Django 4.2.6 on 2023-10-15 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0010_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailings',
            name='user_creator',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
