# Generated by Django 5.0.6 on 2024-05-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dunamis', '0002_alter_job_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='banner',
        ),
    ]
