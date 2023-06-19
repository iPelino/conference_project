from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # www.conference.rw/admin/
    path('admin/', admin.site.urls),
    path('', include('conference.urls'))

]
