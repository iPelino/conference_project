from django.urls import path
from speakers import views

urlpatterns = [
    path('/', views.speaker_list)
    path('create speaker',views.)
    path('/<speaker_id: speakers.id>/' , views.speaker_details),
    path('<int:speaker_id>/update/', views.update_speaker, name='update_speaker'),
    path('<int:speaker_id>/delete/', views.delete_speaker, name='delete_speaker'),
]
