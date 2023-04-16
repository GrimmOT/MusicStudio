# Generated by Django 4.1.5 on 2023-04-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicStudioApp', '0019_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='teacher',
            name='quote',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='work_expirience',
            field=models.IntegerField(default=0),
        ),
    ]
