# Generated by Django 4.1.5 on 2023-03-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicStudioApp', '0007_delete_grade_group_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='surname',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
