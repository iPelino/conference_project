from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference, name='conferences'),
    path('<int:conference_id>/', views.conference_details, name='conference_details'),
    path('<int:conference_id>/update', views.conference_update, name='conference_update_page'),
    path('<int:conference_id>/update/confirm', views.conference_update_confirm, name='conference_update_confirm'),
    path('<int:conference_id>/delete', views.conference_delete, name='conference_delete'),
    path('<int:conference_id>/delete/confirm', views.conference_delete_confirm, name='conference_delete_confirm'),
    path('create/', views.conference_create, name='conference_create_page')
]