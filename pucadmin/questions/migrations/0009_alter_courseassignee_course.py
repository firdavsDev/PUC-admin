# Generated by Django 4.0.5 on 2022-10-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0007_remove_course_gov_slug_course_gov_slugs'),
        ('questions', '0008_alter_question_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseassignee',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignees', related_query_name='assignees', to='organisations.course', verbose_name='course'),
        ),
    ]
