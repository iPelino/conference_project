from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('<int:id>/', views.single_conference),
    path('<int:id>/update/', views.update_conference),
    path('<int:id>/delete/', views.delete_confrence),
    path('create/', views.create_conference)
]