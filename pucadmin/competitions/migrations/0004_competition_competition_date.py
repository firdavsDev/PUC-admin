# Generated by Django 3.2.5 on 2021-07-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_auto_20210715_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_date',
            field=models.DateField(null=True),
        ),
    ]