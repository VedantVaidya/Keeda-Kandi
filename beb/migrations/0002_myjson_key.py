# Generated by Django 5.0.3 on 2025-04-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myjson',
            name='key',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
