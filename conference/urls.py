from django.urls import path, re_path
from conference import views
urlpatterns = [
    path('',views.list_conference,name="lists"),
    path('create/',views.create_conference),
    path('<str:id>/',views.Id_conference),
    path('<str:id>/update',views.list_update),
]