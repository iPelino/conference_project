from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_speakers),
    path('create/', views.create_speaker),
    path('<int:id>/', views.view_single_speaker),
    path('<int:id>/update/', views.update_speaker),
    path('<int:id>/delete/', views.delete_speaker),
]
