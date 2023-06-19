from django.urls import path
from conference_app import views


app_name = 'conference_app'

urlpatterns = [
    path('', views.conference_list, name='conference_list'),
    path('create/', views.create_conference, name='create_conference'),
    path('<int:conference_id>/', views.conference_details, name='conference_details'),
    path('<int:conference_id>/update/', views.update_conference, name='update_conference'),
    path('<int:conference_id>/delete/', views.delete_conference, name='delete_conference'),
]
