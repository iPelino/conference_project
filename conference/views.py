from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
        {
            "id": 1,
            "name": "Introduction to AI",
            "date": "2023-03-12",
            "location": "BK Arena"
        },
        {
            "id": 2,
            "name": "Data Science in health",
            "date": "2023-12-12",
            "location": "Intare Conference Arena"
        },
        {
            "id": 3,
            "name": "Impact of AI on employment",
            "date": "2023-04-02",
            "location": "Hotel Umubano"
        },

        {
            "id": 4,
            "name": "Developing Tech Hubs in Africa",
            "date": "2024-01-01",
            "location": "Intare Conference Arena"
        },

        {
            "id": 5,
            "name": "FIFA Summit 2024",
            "date": "2024-07-01",
            "location": "BK Arena"
        },
    ]
def conferences_view(request):
    return render(request, 'conference/conferences.html', context={"conferences": conferences})

def create_conference_view(request):
    return render(request, "conference/createConference.html")

def conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/conference.html", context={"conference": conference })

def update_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/updateConference.html", context={"conference": conference})

def delete_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/delete_conference.html", context={"conference" : conference})

def confirm_delete_view(request, id):
    return render(request, "conference/confirm_delete.html")