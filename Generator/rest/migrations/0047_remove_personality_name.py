# Generated by Django 4.2.5 on 2023-10-19 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0046_personality_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personality',
            name='name',
        ),
    ]