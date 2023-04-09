from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path
from MusicStudioApp import views 
"""MusicStudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path ('', views.redirect_view ),
    path('admin/', admin.site.urls),
    path('MusicStudio', views.index, name="main"),
    path('MusicStudio/groups/', views.groups_page, name = "groups"),
    path('MusicStudio/groups/<int:group_id>', views.group_view),
    path('MusicStudio/concerts', views.concerts_view, name="concerts"),
    path('MusicStudio/gallery/<int:concert_id>', views.gallery_view, name="gallery"),
    path('MusicStudio/contacts', views.contacts_view, name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)