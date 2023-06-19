from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="conferences"),
    path("new/", views.new)
]