# Generated by Django 4.0 on 2022-01-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_project_likes'),
        ('users', '0008_notification_project_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='liked_projects',
            field=models.ManyToManyField(blank=True, related_name='liked_projects', to='home.Project'),
        ),
    ]
