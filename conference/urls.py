from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="conferences"),
    path("create/", views.New_conference),
    path('<int:id>/', views.conference_by_id),
]
