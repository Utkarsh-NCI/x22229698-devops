# Generated by Django 4.2.11 on 2024-03-29 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_remove_topic_module_module_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='topic',
            new_name='topics',
        ),
    ]