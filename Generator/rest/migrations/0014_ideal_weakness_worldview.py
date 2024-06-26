# Generated by Django 4.2.5 on 2023-10-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0013_rename_race_name_race_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ideal",
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
                ("description", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Weakness",
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
                ("description", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Worldview",
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
                ("name", models.CharField(max_length=15)),
                ("description", models.CharField(max_length=100)),
            ],
        ),
    ]
