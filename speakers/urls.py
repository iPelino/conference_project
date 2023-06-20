from speakers import views
from django.urls import path

urlpatterns = [
    path('speakers/', views.speaker_list),
    path('speakers/ create speaker', views.create_speaker)
]