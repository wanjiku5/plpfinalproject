# Generated by Django 5.0.6 on 2024-05-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dunamis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
