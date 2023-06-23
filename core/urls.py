from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path("conferences/<int:conference_id>/update/",views.update_conf,name='update'),
    path("conferences/<int:conference_id>/delete/",views.delete_conf,name='delete'),
    path("conferences/<int:conference_id>/",views.conf_detail,name='detail'),
    path('conferences/create/',views.new_conf,name='create'),

    path('conferences/',views.all_conf_view,name='conference'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
]