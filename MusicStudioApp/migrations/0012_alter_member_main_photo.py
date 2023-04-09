# Generated by Django 4.1.5 on 2023-03-26 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MusicStudioApp', '0011_group_main_photo_group_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='main_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_photo', to='MusicStudioApp.image'),
        ),
    ]
