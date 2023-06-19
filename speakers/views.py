from django.shortcuts import render
from django.http import HttpResponse

def speakers(request):
    speakers = [
        {'name': 'Jeho', 'bio' : 'IT support', 'contact': '0783243222'},
        {'name': 'Nad', 'bio' : 'IT support', 'contact': '0783243222'},
        {'name': 'John', 'bio' : 'IT support', 'contact': '0783243222'},
        {'name': 'Jenny', 'bio' : 'IT support', 'contact': '0783243222'},
        {'name': 'Jack', 'bio' : 'IT support', 'contact': '0783243222'},
    ]
    return render(request, 'templates/speaker.html', {'speakers': speakers})