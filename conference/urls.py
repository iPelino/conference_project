from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference, name='conference'),
    path('create/', views.create_conference, name='create_conference'),
    path('<int:conference_id>/', views.view_conference, name='view_conference'),
    path('<int:conference_id>/update', views.update_conference, name='update_conference'),
    path('<int:conference_id>/delete', views.delete_conference, name='delete_conference'),
]