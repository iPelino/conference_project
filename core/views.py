from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Conference

def list_conference(request):
    data = Conference.objects.all().values()
    context = { 'my_conference': data }
    return render(request, 'conference_list.html',context)

def Add_conference(request):
    return render(request, 'add_conference.html', )

def single_conference(request, conference_id):
    data = Conference.objects.all().values()
    context = { 'my_conference': data }
    return render(request, 'single_conference.html',context)
    
def update_conference(request, conference_id):
    return render(request, 'conference_form.html')

def remove_conference(request, conference_id):
    items = Conference.objects.all().values()
    context = { 'my_conference': data }
    return render(request, 'remove_conference.html', context)

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
