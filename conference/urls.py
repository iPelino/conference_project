from django.urls import path
from conference import views

urlpatterns = [
    path('conferences/', views.conferences_view),
    path('conferences/create', views.create_conference_view),
    path('conferences/<id>', views.conference_view),
    path('conferences/<id>/update', views.update_conference_view),
    path('conferences/<id>/delete', views.delete_conference_view),
    path('conferences/<id>/delete-confirm', views.confirm_delete_view)
]
