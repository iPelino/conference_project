from speakers import views
from django.urls import  path, include

urlpatterns = [
    path('/', views.view_speakers, name = 'view speakers'),
]