from django.urls import path
from speakers import views

urlpatterns = [
    path('/', views.speaker_list),
    path('/create speaker', views.create_speaker)
    path('<speakers_id:speakers.id>/',view.speaker_details)
]
