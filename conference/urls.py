from django.urls import path, re_path
from conference import views
urlpatterns = [
    path('',views.list_conference,name="lists"),
]