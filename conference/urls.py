from django.urls import path
from conference.views import conferences_view

urlpatterns = [
    path('conferences/', conferences_view)
]
