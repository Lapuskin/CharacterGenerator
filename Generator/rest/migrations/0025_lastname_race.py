# Generated by Django 4.2.5 on 2023-10-11 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0024_remove_lastname_race"),
    ]

    operations = [
        migrations.AddField(
            model_name="lastname",
            name="race",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="rest.race",
            ),
        ),
    ]
