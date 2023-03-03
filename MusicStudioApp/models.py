from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Programm(models.Model):
    text = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.pk} - {self.text}"


class Song(models.Model):
    name = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150, null = True)
    genre = models.ForeignKey(
        'SongGenre',
        on_delete=models.CASCADE,
        default=1
    )
    time = models.TimeField(null = True)

    def __str__(self):
        return f"{self.pk} - {self.name}"
    
class Group(models.Model):
    name = models.CharField(max_length = 150)
    song = models.ManyToManyField(Song, null = True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

class SongGenre(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return f"{self.pk} - {self.name}"

class Instruments(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.pk} - {self.name}"