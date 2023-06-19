from django.urls import path
from . import views

urlpatterns = [
    path('speakers/', views.speakers_view),
    path('speakers/create/', views.create_speaker_view),
    path('speakers/<id>/', views.speaker_view),
    path('speakers/<id>/update/', views.update_speaker_view),
    path('speakers/<id>/delete/', views.delete_speaker_view),
    path('speakers/<id>/delete/delete-confirm/', views.confirm_delete_view)
]
