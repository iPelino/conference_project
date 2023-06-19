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
    conferences = Conference.objects.all()
    return render(request, 'conference/conferences.html', {'conferences': conferences})