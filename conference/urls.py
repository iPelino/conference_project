from django.urls import path, re_path
from conference import views
urlpatterns = [
    path('',views.conference1, name='view_conference'),
    path('<str:id>/', views.conference, name='view_conference'),
    path('<str:id>/update', views.update, name='update'),
    path('<str:id>/delete', views.deleteConf, name='deleteConf'),
    path('create', views.CreateConf, name='create'),
]