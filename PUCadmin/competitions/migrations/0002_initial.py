# Generated by Django 3.2.5 on 2021-07-08 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("schools", "0001_initial"),
        ("competitions", "0001_initial"),
        ("organisations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="supervisor",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="supervisors",
                to="organisations.course",
            ),
        ),
        migrations.AddField(
            model_name="supervisor",
            name="submission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supervisors",
                to="competitions.submission",
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="competition",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="submissions",
                to="competitions.competition",
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="submissions",
                to="organisations.course",
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="school",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="submissions",
                to="schools.school",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="submission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="authors",
                to="competitions.submission",
            ),
        ),
        migrations.AddField(
            model_name="competition",
            name="organisation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="organisations.organisation",
                verbose_name="competitions",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="submission",
            unique_together={("competition", "prize"), ("competition", "title")},
        ),
    ]
