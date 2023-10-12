# Generated by Django 4.2.6 on 2023-10-12 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0006_message_mailings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='mailings',
        ),
        migrations.AddField(
            model_name='mailings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailings.message'),
        ),
    ]