# Generated by Django 4.1.5 on 2023-03-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicStudioApp', '0008_member_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photos',
            field=models.ManyToManyField(blank=True, to='MusicStudioApp.image'),
        ),
    ]
