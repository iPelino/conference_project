from django.shortcuts import render
from django.http import HttpResponse

conferences = [
    {
        "id": 1,
        "name": "community work",
        "date": "2023-09-09",
        "location": "Amsterdam, Netherlands"
    },
    {
        "id": 2,
        "name": "African child celebration",
        "date": "2023-12-01",
        "location": "Rubavu, Rwanda"
    },
    {
        "id": 3,
        "name": "National Independence Day Celebration",
        "date": "2023-07-04",
        "location": "Kigali, Rwanda"
    },
    {
        "id": 4,
        "name": "East African General Meeting",
        "date": "2023-11-05",
        "location": "Kigali, Rwanda"
    },
    {
        "id": 5,
        "name": "National Umushyikirano",
        "date": "2023-12-03",
        "location": "Kigali, Rwanda"
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


def delete_conference (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "delete_conference.html", { "conference": conference })
