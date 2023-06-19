from django.urls import path
from speakers import views

urlpatterns = [
    path('speakers', views.s_list, name = 'speaker_ist'),
    path('speakers/create/', views.s_create, name = 'speaker_create'),
    path('speakers/<speaker_id>', views.s_datails, name = 'speaker_details'),
    path('speakers/<speaker_id>/update', views.s_updates, name = 'speaker_updating'),
    path('speakers/<speaker_id>/delete',views.s_delete, name = 'speaker_')
]