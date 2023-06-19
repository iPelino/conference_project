from speakers import views
from django.urls import  path, include

urlpatterns = [
    path('/', views.view_speakers, name = 'view speakers'),
    path('create_speaker/', views.create_speaker),
    path('<speaker_id: speakers.id>/', views.speaker_detail)
]