"""
URL configuration for conference_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views
from speakers import views

urlpatterns = [
    # www.conference.rw/admin/
    path('admin/', admin.site.urls),
    
    path('speakers/', views.speaker_list, name='speaker_list'),
    path('speakers/create/', views.speaker_create, name='speaker_create'),
    path('speakers/<int:speaker_id>/', views.speaker_detail, name='speaker_detail'),
    path('speakers/<int:speaker_id>/update/', views.speaker_update, name='speaker_update'),
    path('speakers/<int:speaker_id>/delete/', views.speaker_delete, name='speaker_delete'),



    path('', include('core.urls'))

]
