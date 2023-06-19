from django.urls import path
from . import views

urlpatterns = [
    path('conference/', views.list_conference, name='list_conference'),
    path('conference/<int:id>/', views.single_conference, name='single_conference'),
    path('conference/<int:id>/update', views.update_conference, name='update_conference'),
    path('conference/create/', views.Add_conference, name='Add_conference'),
    path('conference/<int:id>/delete', views.remove_conference, name='remove_conference'),
]
