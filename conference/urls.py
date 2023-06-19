from django.urls import path
from . import views

urlpatterns=[
    path('', views.list_of_conference, name='list_of_conference'),
    path('<int:id>/', views.conference_detail, name='conference_detail'),
    path('create/', views.conference_create, name='conference_create'),
    path('<int:id>/update/', views.conference_update, name='conference_update'),
    path('<int:id>/delete/', views.conference_delete, name='conference_delete'),
    ]