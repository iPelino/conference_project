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



def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/conference_list.html', {'conferences': conferences})

def conference_details(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_details.html', {'conference': conference})

def conference_create(request):
    return render(request, 'conference/conference_create.html')

def conference_update(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    return render(request, 'conference/conference_delete.html', {'conference': conference})
