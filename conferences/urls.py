from django.urls import path
from conferences import views

urlpatterns = [
    path('conferences/', views.conferences_available),
path('conferences/create/', views.new_conference), 

]
