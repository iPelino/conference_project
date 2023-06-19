from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),
    path('conferences/', views.conference_list, name='conference_list'),
    path('conferences/<int:conference_id>/', views.conference_details, name='conference_details'),
    path('conferences/create/', views.create_conference, name='create_conference'),
    path('conferences/<int:conference_id>/update/', views.update_conference, name='update_conference'),
    path('conferences/<int:conference_id>/delete/', views.delete_conference, name='delete_conference'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
]
