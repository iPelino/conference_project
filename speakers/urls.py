from django.urls import path
from speakers import views

urlpatterns = [
    path('/', views.speaker_list),
    path('/create speaker', views.create_speaker),
]