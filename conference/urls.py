from django.contrib import admin
from django.urls import path, include
from conference import views

urlpatterns = [
    path('', views.listconference, name='view_conferences'),
    path('create/', views.create_conference, name='create'),
    path('<str:id>/',views.listconferenceId),
    path('<str:id>/update',views.updateconference),

]
