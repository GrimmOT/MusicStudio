from django.shortcuts import render
from django.http import HttpResponse
from MusicStudioApp.models import *

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
    context = {
        "title": "Страница группы",
        "id": group_id
    }
    return render(request, "MusicStudio/group.html", context)