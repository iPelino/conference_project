from django.urls import include, path
from django.contrib import admin
from django.shortcuts import render, redirect
from django.views import View
from conference.views import ConferenceListView, ConferenceDetailView

class ConferenceCreateView(View):
    def get(self, request):
        return render(request, 'conference/conference_create.html')
    
    def post(self, request):
        # Process the submitted form data
        # Save the new conference using the form data
        
        # Redirect to a success page or another URL
        return redirect('conference_list')  # Replace 'conference_list' with the appropriate URL name

class ConferenceListView(View):
    def get(self, request):
        conferences = [
            {'name': 'Conference 1', 'dates': '2023-07-01 to 2023-07-03', 'location': 'City 1'},
            {'name': 'Conference 2', 'dates': '2023-08-05 to 2023-08-07', 'location': 'City 2'},
            {'name': 'Conference 3', 'dates': '2023-09-10 to 2023-09-12', 'location': 'City 3'},
            {'name': 'Conference 4', 'dates': '2023-10-15 to 2023-10-17', 'location': 'City 4'},
            {'name': 'Conference 5', 'dates': '2023-11-20 to 2023-11-22', 'location': 'City 5'},
        ]
        return render(request, 'conference/conference_list.html', {'conferences': conferences})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conferences/', ConferenceListView.as_view(), name='conference_list'),
    path('conferences/create/', ConferenceCreateView.as_view(), name='conference_create'),
    path('conferences/<int:conference_id>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('', include('core.urls')),
]





