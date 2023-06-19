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
]