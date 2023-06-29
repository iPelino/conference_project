from django.urls import path
from conferences import views
urlpatterns = [
    path('', views.conference_list, name='conferences'),
]