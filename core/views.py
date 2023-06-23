from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})
def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")
def testing_stuff(self.request, self.number):

    return render(request, 'testing.html', {'number': number})

def conference_create(self.request):
    return render(self.request, 'conference/conference_create.html')

def conference_detail(self.request, self.conference_id):
    conference = {'name': 'Conference', 'dates': 'October 1-3', 'location': 'City A'}
    return render(self.request, 'conference/conference_detail.html', {'conference': conference})

def conference_update(self.request,self.conference_id):
    conference = {'name': 'Conference', 'dates': 'October 1-3', 'location': 'City A'}
    return render(self.request, 'conference/conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    conference = {'name': 'Conference', 'dates': 'October 1-3', 'location': 'City A'}
    return render(self.request, 'conference/conference_delete.html', {'conference': conference})