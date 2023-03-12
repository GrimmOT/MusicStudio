# Generated by Django 4.1.5 on 2023-03-08 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MusicStudioApp', '0005_group_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MemberGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('grade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MusicStudioApp.membergrade')),
                ('instruments', models.ManyToManyField(null=True, to='MusicStudioApp.instruments')),
                ('photos', models.ManyToManyField(null=True, to='MusicStudioApp.image')),
            ],
        ),
    ]
