from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('conferences/',views.all_conference_view,name='conference'),
    path('conferences/create/',views.new_conference,name='create'),
    path("conferences/<int:conference_id>/",views.conference_detail,name='detail'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),

]
