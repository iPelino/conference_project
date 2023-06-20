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
       conference = conference.objects.get(id=conference_id)
       return render(request, 'conference/conference_detail.html', {'conference': conference})
     
          


 