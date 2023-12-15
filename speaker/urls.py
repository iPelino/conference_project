from django.urls import path
from . import views

urlpatterns = [
    path('speakers/', views.speaker, name='speakers'),
    path('speakers/create', views.speaker, name='create'),
    path('speakers/delete', views.speaker, name='create'),
    path('speakers/update', views.speaker, name='create'),
]