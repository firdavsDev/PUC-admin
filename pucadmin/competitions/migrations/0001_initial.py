# Generated by Django 3.2.5 on 2021-07-08 13:20

import competitions.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competition",
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
                (
                    "name",
                    models.CharField(
                        help_text="For example: Van Melsenprijs 2021", max_length=20
                    ),
                ),
                ("slug", models.SlugField(max_length=20, unique=True)),
                ("registration_start", models.DateTimeField(blank=True, null=True)),
                ("registration_end", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "competition",
                "verbose_name_plural": "competitions",
            },
        ),
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("address_1", models.CharField(blank=True, max_length=100, null=True)),
                ("address_2", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "zip",
                    models.CharField(
                        blank=True,
                        max_length=7,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Enter zip code in this format: '1234 AB'",
                                regex="^[1-9][0-9]{3} (?!SA|SD|SS)[A-Z]{2}",
                            )
                        ],
                    ),
                ),
                ("town", models.CharField(blank=True, max_length=50, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                "verbose_name": "student",
                "verbose_name_plural": "students",
            },
        ),
        migrations.CreateModel(
            name="Submission",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=120, unique=True)),
                ("abstract", models.TextField()),
                (
                    "document",
                    models.FileField(
                        upload_to=competitions.models.submission_upload_path
                    ),
                ),
                ("nominated", models.BooleanField(default=False)),
                ("nomination_report", models.TextField(blank=True)),
                (
                    "nomination_score",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                ("prize", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("jury_report", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "submission",
                "verbose_name_plural": "submissions",
            },
        ),
        migrations.CreateModel(
            name="Supervisor",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("address_1", models.CharField(blank=True, max_length=100, null=True)),
                ("address_2", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "zip",
                    models.CharField(
                        blank=True,
                        max_length=7,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Enter zip code in this format: '1234 AB'",
                                regex="^[1-9][0-9]{3} (?!SA|SD|SS)[A-Z]{2}",
                            )
                        ],
                    ),
                ),
                ("town", models.CharField(blank=True, max_length=50, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                "verbose_name": "supervisor",
                "verbose_name_plural": "supervisors",
            },
        ),
    ]