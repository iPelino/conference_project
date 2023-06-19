from django.urls import path
from conference.views import (
    conference_list,
    conference_create,
    conference_detail,
    conference_update,
    conference_delete
)

urlpatterns = [
    path('conferences/', conference_list, name='conference_list'),
    path('conferences/create/', conference_create, name='conference_create'),
    path('conferences/<int:conference_id>/', conference_detail, name='conference_detail'),
    path('conferences/<int:conference_id>/update/', conference_update, name='conference_update'),
    path('conferences/<int:conference_id>/delete/', conference_delete, name='conference_delete'),
]
