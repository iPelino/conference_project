from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('speakers/', views.speakers_view, name='speakers'),
    path('speakers/create', views.create, name='Create speaker'),
    path('speakers/<int:speaker_id>/',views.speakers_details, name='detail'),
    path('speakers/<int:speaker_id>/update/',views.update_speaker,name='update'),
    path('speakers/<int:speaker_id>/delete/',views.delete_speaker,name='delete'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
]