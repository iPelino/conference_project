# urls.py
from django.urls import path
from .views import conference_list, conference_detail, create_conference

urlpatterns = [
    path('', conference_list, name='conference_list'),
    path('<int:pk>/', conference_detail, name='conference_detail'),
    path('create/', create_conference, name='create_conference'),
]

