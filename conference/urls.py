from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_view),
    path('conferences/create', views.create_conference_view),
    path('conferences/<id>', views.conference_id),
    path('conferences/<<conference_id>/update', views.update),
]