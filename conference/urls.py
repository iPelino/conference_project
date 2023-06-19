from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_list),
     path('conferences/create/', views.create_new_conference),
   
]
