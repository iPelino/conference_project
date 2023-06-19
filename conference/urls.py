from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_list),
     path('conferences/create/', views.create_new_conference),
      path('conferences/<id>/', views.conference_view),
       path('conferences/<id>/update/', views.update_conference),
        path('conferences/<id>/delete/', views.delete_conference),
   
]
