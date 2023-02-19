from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length = 150)


class Grade(models.Model):
    name = models.CharField(max_length = 150)


class Programm(models.Model):
    text = models.CharField(max_length = 150)


class Song(models.Model):
    name = models.CharField(max_length = 150)


class Instruments(models.Model):
    name = models.CharField(max_length = 150)
