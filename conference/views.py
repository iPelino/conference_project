from django.shortcuts import render
from django.http import HttpResponse

conferences = [
    {
        "id": 1,
        "name": "International Malaria Yearly Conference",
        "date": "09/09/2023",
        "location": "Amsterdam, Netherlands"
    },
    {
        "id": 2,
        "name": "InterPol Peace Keeping Conference",
        "date": "01/12/2023",
        "location": "Musanze, Rwanda"
    },
    {
        "id": 3,
        "name": "National Liberation Day Celebration",
        "date": "04/07/2023",
        "location": "Kigali, Rwanda"
    },
    {
        "id": 4,
        "name": "East African General Meeting",
        "date": "05/11/2023",
        "location": "Kigali, Rwanda"
    },
    {
        "id": 5,
        "name": "National Umushyikirano",
        "date": "03/12/2023",
        "location": "Kigali, Rwanda"
    }
]


def index(request):
    return render (request, "index.html", {'conferences': conferences})


def create(request):
    return render (request, "create_conference.html")


