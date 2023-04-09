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
    member = models.ManyToManyField('Member', null = True)
    main_photo = models.ForeignKey(
        'Image',
        null=True,
        on_delete=models.CASCADE,
        related_name = "main_group_photo"
    )
    photos = models.ManyToManyField('Image', null = True, related_name = "group_photos")

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

    def __str__(self):
        start = self.src.url.rfind("/")
        end = self.src.url.rfind(".")
        return f"{self.pk} - {self.src.url[start + 1 : end]}"


class Member(models.Model):
    name = models.CharField(max_length = 150)
    surname = models.CharField(max_length = 150, null = True)
    instruments = models.ManyToManyField(Instruments, null = True)
    grade = models.ForeignKey(
        'MemberGrade',
        on_delete=models.CASCADE,
        default=1
    )
    photos = models.ManyToManyField(
        Image, blank = True,
        related_name = "photos")
    main_photo = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name = "main_photo" 
    )
    def __str__(self):
        return f"{self.pk} - {self.surname} {self.name} {self.grade.name}"
    

class Concert(models.Model):
    name = models.CharField(max_length = 150)
    photos = models.ManyToManyField(
        Image, blank = True,
        related_name = "concerts_photos")
    video = models.CharField(max_length = 150)
    def __str__(self):
        return f"{self.pk} - {self.name}"