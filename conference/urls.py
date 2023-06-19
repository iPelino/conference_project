from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conference/<int:conference_id>', views.conference_details, name='conference_details'),
    path('conference/<int:conference_id>/update', views.update_page, name='conference_update_page')
]