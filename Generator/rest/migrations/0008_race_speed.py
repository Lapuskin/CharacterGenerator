# Generated by Django 4.2.5 on 2023-10-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0007_race_maturity_race_youth"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="speed",
            field=models.IntegerField(default=0),
        ),
    ]
