# Generated by Django 5.1.1 on 2024-10-22 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-updated_on"]},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="title",
        ),
    ]