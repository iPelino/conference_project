from django.urls import path
from . import views

app_name = 'speakers'

urlpatterns = [
    path('', views.speakers_list, name='speakers_list'),
    path('speakers/create/', views.speaker_create, name='speaker_create'),
    path('speakers/<int:speaker_id>/', views.speaker_detail, name='speaker_detail'),
    path('speakers/<int:speaker_id>/update/', views.speaker_update, name='speaker_update'),
    path('speakers/<int:speaker_id>/delete/', views.speaker_delete, name='speaker_delete'),
]
