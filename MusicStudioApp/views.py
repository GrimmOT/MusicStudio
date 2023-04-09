from django.shortcuts import render
from django.http import HttpResponse
from MusicStudioApp.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/MusicStudio')
    return response


# Create your views here.
def index(request):
    context = {
        "title": "Музыкальная Студия",
        "content": "This is content"
    } 
    return render(request, "MusicStudio/index.html", context)


def groups_page(request):
    groups = Group.objects.all()
    print(groups)
    context = {
        "title": "Группы",
        "groups": groups
    } 
    return render(request, "MusicStudio/groups.html", context)


def group_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    songs = group.song.all()
    members = group.member.all()
    img = Image.objects.get(pk=23)
    print(songs)
    print(members)
    context = {
        "title": "Страница группы",
        "id": group_id,
        "songs": songs,
        "group": group,
        "members": members,
        "placeholder": img
    }
    return render(request, "MusicStudio/group.html", context)


def concerts_view(request):
    img = Image.objects.get(pk=23)
    concerts = Concert.objects.all()
    context = {
        "concerts": concerts,
        "placeholder": img
    }
    return render(request, "MusicStudio/concerts.html", context)


def gallery_view(request, concert_id):
    if concert_id == -1:
        pass
    else:
        concert = get_object_or_404(Concert, pk=concert_id)
        photos = concert.photos.all()
    context = {
        "concert": concert,
        "photos": photos
    }
    return render(request, "MusicStudio/gallery.html", context)


def contacts_view(request):
    context = {

    }
    return render(request, "MusicStudio/gallery.html", context)