from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_list),
   
]
