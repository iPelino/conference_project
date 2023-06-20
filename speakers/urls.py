from speakers import views
from django.urls import path

urlpatterns = [
    path('speakers/', views.speaker_list),
]