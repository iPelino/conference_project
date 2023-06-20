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
    path("speakers/",views.speaker,name="all speakers"),
    path("speakers/<str:pk>/",views.individualspeaker,name="individual speaker"),
    path("speakers/<str:pk>/update/",views.updatespeaker,name="update speaker"),
    path("speakers/<str:pk>/delete/",views.deletespeaker,name="delete speaker"),
    path("speakers/create/",views.createspeaker,name="create speaker"),
]