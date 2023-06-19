from django.urls import path
from . import views

urlpatterns = [
    path('conferences/',views.list_conferences,name="List of Conferences"),
    path('conferences/create/',views.create_new),
    path('conferences/create/conferences.html',views.list_conferences),
    path('conferences/create/create.html',views.create_new)

]