from django.urls import path, re_path
from core import views
from django.urls import include


app_name = 'conference'

urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    path('conferences/', include('conference.urls')),

    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
    path('', views.conference_list, name='conference_list'),
    path('create/', views.conference_create, name='conference_create'),
    path('<int:conference_id>/', views.conference_details, name='conference_details'),
    path('<int:conference_id>/update/', views.conference_update, name='conference_update'),
    path('<int:conference_id>/delete/', views.conference_delete, name='conference_delete'),
]





