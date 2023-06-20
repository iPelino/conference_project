from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),

    path('conferences/', views.all_conferences, name='all_conferences'),
    path('conferences/create/', views.new_conference, name='new_conference'),
    path('conferences/<int:conference_id>/', views.conference_detail, name='conference_detail'),
    path('conference/<int:conference_id>/update', views.conference_update, name='conference_name'),
    path('conference/<int:confference_id>/delete/', views/.conference_delete, name='conference_delete'),
]