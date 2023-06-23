from django.http import HttpResponse
from django.shortcuts import render


conferences = [{'conference_id':1,'conference_name':'CHOGM','date':'Mon, Jun 20, 2022 - Sun, Jun 26, 2022','location':'Kigali Convention Center','topic':'General meeting'},
            {'conference_id':2,'conference_name':'YouthConnekt Africa','date':'Oct 15, 2022','location':'BK Arena' ,'topic':'African Youth meeting '},
            {'conference_id':3,'conference_name':'Commonwealth of Nations','date':'Mon, Mar 13, 2023','location':'Kigali Convention Centery' ,'topic':'Nation meet'},]
def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request):
     return render(request, 'testing.html', {'data': conferences})

def create_view(request):
    data = ['create']
    return render(request, 'create.html', {'data': data})

def viewParticular(request,id):
    data = {}
    for conference in conferences:
        if conference['conference_id']==id:
          data=conference
    return render(request, 'singleConference.html', {'data': data})

def update(request,id):
    data = {}
    for conference in conferences:
        if conference['conference_id']==id:
          data=conference
    return render(request, 'updateConference.html', {'data': data})

def delete(request,id):
    data = {}
    for conference in conferences:
        if conference['conference_id']==id:
          data=conference
    return render(request, 'deleteConference.html', {'data': data})