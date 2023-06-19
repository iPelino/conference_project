from django.urls import include, path

urlpatterns = [
    # Other URL patterns
    path('speakers/', include('speakers.urls')),
]
