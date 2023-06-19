from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="conferences"),
    path("create/", views.create),
    path('<int:id>/', views.single_conference),
    path('<int:id>/update', views.update_conference),
]