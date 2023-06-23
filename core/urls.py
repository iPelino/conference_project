from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('conferences/', views.testing_stuff, name='testing'),
    # path('<pk:id>/', views.testing_stuff, name='testing'),
    # path('<slug:slug>/', views.testing_stuff, name='testing'),

    # www.conference.rw/about/
    path('about/', views.about_view, name='about'),
    
    # www.conference.rw/references/create/
    path('conferences/create/', views.create_view, name='create'),

    path('conferences/<int:id>/', views.viewParticular, name='create'),
    path('conferences/<int:id>/update', views.update, name='create'),
    
    path('conferences/<int:id>/delete', views.delete, name='create'),

]