# Generated by Django 4.2.5 on 2023-09-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms_app', '0003_tasks_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='in_team',
            field=models.BooleanField(default=False),
        ),
    ]