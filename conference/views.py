from django.shortcuts import render
from django.http import HttpResponse

conferences = [
    {
        "id": 1,
        'name': 'PyCon UK',
        'city': 'Birmingham',
        'country': 'UK',
        'date': '2021-09-17',
        'url': 'https://2021.pyconuk.org/'
    },
    {
        "id": 2,
        'name': 'PyCon India',
        'city': 'Hyderabad',
        'country': 'India',
        'date': '2021-09-25',
        'url': 'https://in.pycon.org/2021/'
    },
    {
        "id": 3,
        'name': 'PyCon Australia',
        'city': 'Sydney',
        'country': 'Australia',
        'date': '2021-08-06',
        'url': 'https://2021.pycon-au.org/
    },
    {
        "id": 4,
         'name': 'PyCon Canada',
        'city': 'Toronto',
        'country': 'Canada',
        'date': '2021-11-12',
        'url': 'https://2021.pycon.ca/'
    },
    {
        "id": 5,
         'name': 'PyCon France',
        'city': 'Paris',
        'country': 'France',
        'date': '2021-10-08',
        'url': 'https://www.pycon.fr/'
    }
]


def index(request):
    return render (request, "index.html", {'conferences': conferences})


def create(request):
    return render (request, "create_conference.html")


def single_conference (request, id: int): 
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "single_conference.html", { "conference": conference })


def update_conference (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "update_conference.html", { "conference": conference })
