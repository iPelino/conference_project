from django.urls import path
from speakers import views

urlpatterns = [
    path('/', views.speaker_list),
    path('/create speaker', views.create_speaker),
    path('/speaker details', views.speaker_details),
    path('/update speaker', views.update_speaker),
]