from django.urls import path
from . import views

app_name = 'speakers'

urlpatterns = [
    path('', views.SpeakerListView.as_view(), name='speaker_list'),
    path('create/', views.SpeakerCreateView.as_view(), name='speaker_create'),
    path('<int:speaker_id>/', views.SpeakerDetailView.as_view(), name='speaker_detail'),
    path('<int:speaker_id>/update/', views.SpeakerUpdateView.as_view(), name='speaker_update'),
    path('<int:speaker_id>/delete/', views.SpeakerDeleteView.as_view(), name='speaker_delete'),
]
