from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
{
  "id": 1,
  "name": "Introduction to Tech In Farming",
  "date": "2023-03-12",
  "location": "Eiffel Tower Conference Center"
},
{
  "id": 2,
  "name": "Data Science in Healthcare",
  "date": "2023-12-12",
  "location": "Louvre Museum Auditorium"
},
{
  "id": 3,
  "name": "Impact of Technology on Employment",
  "date": "2023-04-02",
  "location": "Champs-Élysées Convention Hall"
},
{
  "id": 4,
  "name": "Developing Tech Ecosystem in France",
  "date": "2024-01-01",
  "location": "La Défense Technology Park"
},
{
  "id": 5,
  "name": "Paris Tech Summit 2024",
  "date": "2024-07-01",
  "location": "Palais des Congrès"
}
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