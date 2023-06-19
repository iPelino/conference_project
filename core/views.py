from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})

def conference_list(request):
    data=[
    {"id": 1.0,'name': 'Conference A','dates': '12th may 2023','location': 'Area A'},
    {"id": 1.1,'name': 'Conference B','dates': '1st January 1990 to 5th  February 1995.','location': 'Area B'},
    {"id": 1.2,'name': 'Conference C','dates': '23rd January 1999 to 5th  March 19999','location': 'Area C'},
    {"id": 1.3,'name': 'Conference D','dates': '1st January 2000 to 5th  February 2000','location': 'Area D'},
    {"id": 1.4,'name': 'Conference E','dates': '21st January 20223 to 25th January 2023','location': 'Area E'}]
    return render(request,'conference.html',{"data":data})

def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})
