from django.contrib import admin


from .models import *

admin.site.register(Group)

admin.site.register(Grade)

admin.site.register(Song)

admin.site.register(Programm)

admin.site.register(Instruments)