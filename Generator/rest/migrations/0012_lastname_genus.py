# Generated by Django 4.2.5 on 2023-10-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0011_firstname_lastname_delete_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="lastname",
            name="genus",
            field=models.CharField(default="", max_length=30),
        ),
    ]
