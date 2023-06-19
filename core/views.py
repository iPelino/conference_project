from django.http import HttpResponse
from django.shortcuts import render
from .models import Conference


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})


def all_conferences(request):
    conferences = [
        {'name': 'Conference May', 'dates': '2023-05-23', 'location': 'City A', 'topic': 'Project A'},
        {'name': 'Conference June', 'dates': '2023-06-26', 'location': 'City B', 'topic': 'Project B'},
        {'name': 'Conference July', 'dates': '2023-07-20', 'location': 'City C', 'topic': 'Project C'},
        {'name': 'Conference August', 'dates': '2023-08-09', 'location': 'City D', 'topic': 'Project D'},
        {'name': 'Conference November', 'dates': '2023-11-12', 'location': 'City E', 'topic': 'Project E'},
    ]
    return render(request, 'conference/conferences.html', {'conferences': conferences})

def new_conference(request):
    return render(request, 'conference/new_conference.html')

def conference_detail(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_detail.html', {'conference': conference})

def conference_update(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_delete.html', {'conference': conference})