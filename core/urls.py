from django.urls import path, re_path
from speakers import views


urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
     path('speakers/', include('speakers.urls')),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),
    path('', views.speaker_list, name='speaker_list'),
    path('create/', views.speaker_create, name='speaker_create'),
    path('<int:speaker_id>/', views.speaker_detail, name='speaker_detail'),
    path('<int:speaker_id>/update/', views.speaker_update, name='speaker_update'),
    path('<int:speaker_id>/delete/', views.speaker_delete, name='speaker_delete'),
    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
]