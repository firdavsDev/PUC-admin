# Generated by Django 3.2.5 on 2021-08-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0010_auto_20210326_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idp',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='idpattribute',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='idpuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='idpuserdefaultvalue',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
