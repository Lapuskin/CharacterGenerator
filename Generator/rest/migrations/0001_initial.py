# Generated by Django 4.2.5 on 2023-10-05 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Background",
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
                ("title", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Class",
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
                ("name", models.CharField(max_length=100)),
                ("features", models.CharField(max_length=300)),
                ("link", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Peculiarities",
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
            name="Race",
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
                ("race_name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("force_bonus", models.IntegerField()),
                ("dexterity_bonus", models.IntegerField()),
                ("endurance_bonus", models.IntegerField()),
                ("wisdom_bonus", models.IntegerField()),
                ("intelligence_bonus", models.IntegerField()),
                ("charisma_bonus", models.IntegerField()),
                ("link", models.CharField(max_length=100)),
                ("min_height", models.IntegerField()),
                ("min_weight", models.IntegerField()),
                ("max_height", models.IntegerField()),
                ("max_weight", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Personality",
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
                ("abbreviation", models.CharField(max_length=6)),
                ("meaning", models.CharField(max_length=300)),
                ("class_id", models.ManyToManyField(to="rest.class")),
            ],
        ),
        migrations.CreateModel(
            name="Name",
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
                ("name", models.CharField(max_length=100)),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rest.race"
                    ),
                ),
            ],
        ),
    ]
