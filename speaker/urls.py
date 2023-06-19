from django.urls import path
from speaker import views

urlpatterns = [ 
    path('speakers/', views.speakers_view),
    path('speakers/create', views.create_cspeaker_view),
    path('speakers/<id>',views.speaker_id),
    path('speakers/<id>/update',views.cspeaker_update)
   
]