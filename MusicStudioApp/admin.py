from django.contrib import admin


from .models import *

admin.site.register(Group)

admin.site.register(Song)

admin.site.register(SongGenre)

admin.site.register(Programm)

admin.site.register(Instruments)

admin.site.register(Member)

admin.site.register(Image)

admin.site.register(MemberGrade)

admin.site.register(Concert)