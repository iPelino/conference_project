from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_view),
    path('conferences/create', views.create_conference_view)
]
