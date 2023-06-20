from speakers import views
from django.urls import path

urlpatterns = [
    path('speakers/', views.speaker_list),
    path('speakers/create speaker', views.create_speaker),
    path('speakers/speaker details', views.speaker_details),
    path('speakers/speaker update', views.update_speaker),
    path('speakers/speaker delete', views.delete_speaker)
]