# Generated by Django 4.2.5 on 2023-10-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0016_rename_name_race_race_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lastname",
            name="race",
        ),
        migrations.AddField(
            model_name="lastname",
            name="race",
            field=models.ManyToManyField(to="rest.race"),
        ),
    ]