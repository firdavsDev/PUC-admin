# Generated by Django 3.2.5 on 2021-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organisations", "0004_auto_20210718_1147"),
        ("schools", "0005_alter_school_courses_offered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="courses_offered",
            field=models.ManyToManyField(
                blank=True,
                related_name="schools",
                related_query_name="schools",
                to="organisations.Course",
                verbose_name="courses",
            ),
        ),
    ]
