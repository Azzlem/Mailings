# Generated by Django 4.2.6 on 2023-10-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0019_alter_mailings_user_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailings',
            name='user_creator',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='создатель'),
        ),
    ]