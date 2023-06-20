from requests import request
import conference_project
from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view():
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})

def all_conferences(request):
      conferences = conference_project.objects.all()  
      return render(request, 'conference/conferences.html', {'conferences': conferences})
    
def new_conference(request):
        return render(request, 'conference/new_conference.html')

def conference_details(request, conference_id):
       conference = {"name": "Conference 1", "dates": "March 1-3, 2023", "location": "Kacyiru"}
       conference = {"name": "Conference 2", "dates": "March 1-3, 2023", "location": "Nyamata"}
       conference = {"name": "Conference 3", "dates": "March 1-3, 2023", "location": "Huye"}
       conference = {"name": "Conference 4", "dates": "March 1-3, 2023", "location": "Muhanga"}
       return render(request, 'conference/conference_detail.html', {'conference': conference})
     

def conference_update(request, conference_id):
      conference = conference.objects.get(id=conference_id)
      return render(request, 'conference/conference_updates.html', {'conference': conference})    
          
def conference_delete(request, conference_id):
      conference = conference.objects.get(id=conference_id)
      return render(request, 'conference/conference_delete.html', {'conference': conference})

 