from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.gatenga.rw
    path('', views.home_view, name='home'),
    path('gatenga/',views.all_gatenga_view,name='gatenga'),
      path('gatenga/create/',views.create_gatenga,name='create'),
       path("gatenga/<int:gatenga_id>/details/",views.gatenga_detail,name='detail'),
        path("gatenga/<int:gatenga_id>/update/",views.update_gatenga,name='update'),
         path("gatenga/<int:gatenga_id>/delete/",views.delete_gatenga,name='delete'),



    path('<str:number>/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),

]
