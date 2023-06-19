# urls.py
from django.urls import path
from .views import conference_list, conference_detail, create_conference, delete_conference, edit_conference

urlpatterns = [
    path('', conference_list, name='conference_list'),
    path('conference/<int:pk>/', conference_detail, name='conference_detail'),
    path('conference/create/', create_conference, name='create_conference'),
    path('conference/<int:pk>/delete/', delete_conference, name='delete_conference'),
     path('conference/conference/<int:pk>/edit/', edit_conference, name='edit_conference'),
]

