from django.urls import path
from Speakers import views

urlpatterns = [
    path('Speakers/', views.speaker_view),
    path('Speakers/create', views.create_speaker_view),
    path('Speakers/<id>', views.speaker_view),
    path('Speakers/<id>/update', views.update_speaker_view),
    path('Speakers/<id>/delete', views.delete_speaker_view),
    path('Speakers/<id>/delete-confirm', views.confirm_delete_view)
]
