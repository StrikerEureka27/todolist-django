# Generated by Django 5.0.2 on 2024-03-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
