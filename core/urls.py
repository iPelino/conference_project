from django.urls import path
from conference.views import (
    ConferenceListView,
    ConferenceCreateView,
    ConferenceDetailView,
    ConferenceUpdateView,
    ConferenceDeleteView,
)

urlpatterns = [
    path('conferences/', ConferenceListView.as_view(), name='conference_list'),
    path('conferences/create/', ConferenceCreateView.as_view(), name='conference_create'),
    path('conferences/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('conferences/<int:pk>/update/', ConferenceUpdateView.as_view(), name='conference_update'),
    path('conferences/<int:pk>/delete/', ConferenceDeleteView.as_view(), name='conference_delete'),
]
