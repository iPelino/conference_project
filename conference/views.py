from django.shortcuts import render
from django.http import HttpResponse

conferences = [
    {
        "id": 1,
        "name": "Python yearly conference",
        "date": "2020-10-05",
        "location": "California",
        "topic": "Frameworks maintenance"
    },
    {
        "id": 2,
        "name": "Global Monetary fund conference",
        "date": "2023-11-21",
        "location": "London",
        "topic": "paying back loans"
    },
    {
        "id": 3,
        "name": "Rwanda day celebration",
        "date": "2023-12-05",
        "location": "Brussels",
        "topic": "Meeting with Brussels diaspora"
    },
    {
        "id": 4,
        "name": "Uganda National Independence Celebration",
        "date": "2023-11-09",
        "location": "Kampala",
        "topic": "Uganda's future generation"
    },
    {
        "id": 5,
        "name": "National Umushyikirano Event",
        "date": "2023-12-10",
        "location": "Kigali, Rwanda",
        "topic": "Umushyikirano"
    }
]


def index(request):
    return render (request, "index.html", {'conferences': conferences})


def create(request):
    return render (request, "create.html")


def single_conference (request, id: int): 
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "singleConference.html", { "conference": conference })


def update_conference (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "update.html", { "conference": conference })


def delete_conference (request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render (request, "delete.html", { "conference": conference })

