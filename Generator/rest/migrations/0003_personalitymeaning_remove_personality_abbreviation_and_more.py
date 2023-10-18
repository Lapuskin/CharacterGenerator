# Generated by Django 4.2.5 on 2023-10-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0002_remove_personality_class_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalityMeaning",
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
                ("letter", models.CharField(max_length=1)),
                ("meaning", models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name="personality",
            name="abbreviation",
        ),
        migrations.RemoveField(
            model_name="personality",
            name="meaning",
        ),
        migrations.AddField(
            model_name="personality",
            name="first_letter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="first_letter_personality",
                to="rest.personalitymeaning",
            ),
        ),
        migrations.AddField(
            model_name="personality",
            name="fourth_letter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="fourth_letter_personality",
                to="rest.personalitymeaning",
            ),
        ),
        migrations.AddField(
            model_name="personality",
            name="second_letter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="second_letter_personality",
                to="rest.personalitymeaning",
            ),
        ),
        migrations.AddField(
            model_name="personality",
            name="third_letter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="third_letter_personality",
                to="rest.personalitymeaning",
            ),
        ),
    ]
