# Generated by Django 4.2.11 on 2024-03-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modules", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
