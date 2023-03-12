from django.db import models

# Create your models here.

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

class MemberGrade(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return f"{self.pk} - {self.name}"

class Image(models.Model):
    src = models.ImageField()

class Member(models.Model):
    name = models.CharField(max_length = 150)
    instruments = models.ManyToManyField(Instruments, null = True)
    grade = models.ForeignKey(
        'MemberGrade',
        on_delete=models.CASCADE,
        default=1
    )
    photos = models.ManyToManyField(Image, null = True)

