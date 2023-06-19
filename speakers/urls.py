from django.urls import path
from . import views

urlpatterns=[
    path('', views.list_of_speaker, name='list_of_speakers'),
    path('<int:id>/', views.speaker_detail, name='speaker_detail'),
    path('create/', views.speaker_create, name='speaker_create'),
    path('<int:id>/update/', views.speaker_update, name='speaker_update'),
    path('<int:id>/delete/', views.speaker_delete, name='speaker_delete'),
    ]
