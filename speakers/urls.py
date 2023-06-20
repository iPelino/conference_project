from django.urls import path
from speakers import views

urlpatterns = [
 path('/', views.speaker_list),
 path('/<speaker_id: speakers.id>/',views.speaker_details)
] 
