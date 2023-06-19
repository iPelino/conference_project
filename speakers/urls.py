from django.urls import path
from speakers import views

urlpatterns = [
    path('speakers/', views.speakers_view),
    path('speakers/create/', views.create_speaker_view),
    
]
