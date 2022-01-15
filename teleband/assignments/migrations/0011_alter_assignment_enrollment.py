# Generated by Django 3.2.11 on 2022-01-13 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_alter_enrollment_unique_together"),
        ("assignments", "0010_auto_20220113_1401"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignment",
            name="enrollment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="courses.enrollment"
            ),
        ),
    ]