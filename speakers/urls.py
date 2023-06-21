from django.urls import path
urlpatterns = [
    # www.conference.rw
    path('',views.home,name="home"),
  path('speakers/',views.speaker,name='all speaker'),
  path('speakers/<str:pk>/',views.individualspeaker,name="individualspeaker"),
  path('speakers/<str:pk>/update/',views.updatespeaker,name="updatespeaker"),
  path('speakers/<str:pk>/delete/',views.deletespeaker,name="deletespeaker"),
  path('speaker/create/',views.createspeaker,name="create speaker")
]