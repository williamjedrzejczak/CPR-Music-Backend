# Generated by Django 3.2.11 on 2022-01-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="slug",
            field=models.SlugField(default="slug"),
            preserve_default=False,
        ),
    ]
