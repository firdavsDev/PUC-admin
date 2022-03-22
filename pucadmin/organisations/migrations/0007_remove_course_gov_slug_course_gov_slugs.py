# Generated by Django 4.0 on 2022-03-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0006_course_gov_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='gov_slug',
        ),
        migrations.AddField(
            model_name='course',
            name='gov_slugs',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='government slugs'),
        ),
    ]