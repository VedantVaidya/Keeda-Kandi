# Generated by Django 5.0.4 on 2024-05-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("json_store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WAXpathJson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("xpaths", models.TextField()),
            ],
            options={
                "db_table": "WAXpathJson",
            },
        ),
    ]
