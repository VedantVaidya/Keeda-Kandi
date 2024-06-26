# Generated by Django 5.0.3 on 2024-06-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WAScriptJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('python', models.TextField()),
                ('html', models.TextField()),
                ('css', models.TextField()),
                ('js', models.TextField()),
            ],
            options={
                'db_table': 'WAScriptJson',
            },
        ),
        migrations.CreateModel(
            name='WAXpathJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('xpaths', models.TextField()),
            ],
            options={
                'db_table': 'WAXpathJson',
            },
        ),
        migrations.CreateModel(
            name='WifiJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'WifiJson',
            },
        ),
    ]
