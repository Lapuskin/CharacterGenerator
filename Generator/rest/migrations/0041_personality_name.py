# Generated by Django 4.2.5 on 2023-10-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0040_rename_race_race_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]