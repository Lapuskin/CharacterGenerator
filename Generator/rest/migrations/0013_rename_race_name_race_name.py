# Generated by Django 4.2.5 on 2023-10-10 21:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0012_lastname_genus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="race",
            old_name="race_name",
            new_name="name",
        ),
    ]
