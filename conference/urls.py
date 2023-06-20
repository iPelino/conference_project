from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_conferences),
    path('conferences/', views.all_conferences),
    path('conferences/create/', views.create_conference),
    path('conferences/<int:id>/', views.view_single_conference),
    path('conferences/<int:id>/update/', views.update_conference),
    path('conferences/<int:id>/delete/', views.delete_conference),
]
