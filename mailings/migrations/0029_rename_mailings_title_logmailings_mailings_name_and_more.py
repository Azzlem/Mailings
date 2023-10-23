# Generated by Django 4.2.6 on 2023-10-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0028_alter_logmailings_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logmailings',
            old_name='mailings_title',
            new_name='mailings_name',
        ),
        migrations.RenameField(
            model_name='logmailings',
            old_name='mailing_text',
            new_name='message_text',
        ),
        migrations.AddField(
            model_name='logmailings',
            name='message_title',
            field=models.CharField(blank=True, null=True, verbose_name='заголовок сообщения'),
        ),
    ]