from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request):
     data = [{'conference_id':1,'conference_name':'CHOGM','date':'Mon, Jun 20, 2022 - Sun, Jun 26, 2022','location':'Kigali Convention Center'},
            {'conference_id':2,'conference_name':'YouthConnekt Africa','date':'Oct 15, 2022','location':'BK Arena'},
            {'conference_id':3,'conference_name':'Commonwealth of Nations','date':'Mon, Mar 13, 2023','location':'Kigali Convention Centery'},]
     return render(request, 'testing.html', {'data': data})

def create_view(request):
    data = ['create']
    return render(request, 'create.html', {'data': data})