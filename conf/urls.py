from django.urls import path, re_path
from conf import views
urlpatterns = [
    # conference
    path('speakers/', views.speakers_view,name='speakers'),
    path('speakers/create', views.create,name='createspeaker'),
    path('speakers/<id>', views.speaker,name='speaker'),
    path('speakers/<id>/update', views.update_speaker,name='updatespeaker'),
    path('speakers/<id>/delete', views.delete_speaker,name='deletespeaker'),
     path('speakers/<id>/confirm_delete', views.delete_speaker_confirm,name='deletespeaker'),
    

]