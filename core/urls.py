from django.urls import path, re_path
from core import views
urlpatterns = [
    # /conferences/
    path('', views.render_conference_list, name='home'),
    path('create/', views.create_conference, name='scheduler'),
    path('<int:conference_id>/', views.render_conference, name="conference details"),
    path('<int:conference_id>/update/', views.update_conference, name="conference update"),
    path('<int:conference_id>/delete/', views.delete_conference, name="conference removal")
]
