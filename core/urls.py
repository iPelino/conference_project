from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.render_conference_list, name='home'),
    
]

    # path('<str:number>/', views.testing_stuff, name='testing'),
    # path('about/', views.about_view, name='about'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/