# Generated by Django 4.2.5 on 2023-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0041_personality_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personality',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
