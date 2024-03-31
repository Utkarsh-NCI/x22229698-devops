# Generated by Django 4.2.11 on 2024-03-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_remove_module_topics_topic_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
