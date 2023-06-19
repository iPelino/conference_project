from django.urls import path
from speakers import views
urlpatterns = [
    path('/', views.speaker),
    path('create_speaker/', views.create_speaker),
    path('/<speaker_id: speakers.id>/' , views.speaker_details),
]
