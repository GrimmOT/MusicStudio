from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "title": "Музыкальная Студия",
        "content": "This is content"
    } 
    return render(request, "MusicStudio/index.html", context)