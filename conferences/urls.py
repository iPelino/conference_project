from django.urls import path
from conferences import views


urlpatterns = [
    path('conferences/', views.conferences_available),
    path('conferences/create/', views.new_conference), 
    path('conferences/<id>/', views.conference_view),
    path('conferences/<id>/update/', views.update_conference_view),
    path('conferences/<id>/delete/', views.delete_conference_view),

]
