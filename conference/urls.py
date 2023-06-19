from django.contrib import admin
from django.urls import path, include
from conference import views

urlpatterns = [
    path('', views.listconference, name='view_conferences'),

]
