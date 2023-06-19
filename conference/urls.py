from django.urls import path
from conference import views

app_name = 'conference'

urlpatterns = [
    path('conferences/', views.conference_list, name='conference_list'),
    path('conferences/create/', views.conference_create, name='conference_create'),
    path('conferences/<int:conference_id>/', views.conference_details, name='conference_details'),
    path('conferences/<int:conference_id>/update/', views.conference_update, name='conference_update'),
    path('conferences/<int:conference_id>/delete/', views.conference_delete, name='conference_delete'),
]
