# Generated by Django 4.2.6 on 2023-10-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0021_alter_mailings_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntersectionMailingsClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.client')),
                ('mailings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailings')),
            ],
        ),
    ]
