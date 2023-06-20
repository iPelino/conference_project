from django.shortcuts import render
from django.http import HttpResponse

conferences = [
    {
        "id": 1,
        "name": "National AIDS day",
        "date": "2021-03-09",
        "location": "Kigali"
    },
    {
        "id": 2,
        "name": "Kwita Izina celebration",
        "date": "2023-11-12",
        "location": "Musanze"
    },
    {
        "id": 3,
        "name": "Rwanda Boxing sports day",
        "date": "2023-01-12",
        "location": "Muhanga"
    },
    {
        "id": 4,
        "name": "Umushyikirano",
        "date": "2023-12-12",
        "location": "Kigali"
    },
    {
        "id": 5,
        "name": "Women's day celebration",
        "date": "2022-02-08",
        "location": "Ruhango"
    }
]


def index(request):
    return render (request, "index.html", {'conferences': conferences})


def New_conference(request):
    return render (request, "conference_create.html")


def conference_by_id (request, id: int): 
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "singleConference.html", { "conference": conference })


def update (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "conferenceUpdate.html", { "conference": conference })


def delete (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "deleteConference.html", { "conference": conference })
