from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "EAC MEETING",
        "date": "02-09-2023",
        "city": "KIGALI",
        "attendees": 800,
    },
    {
        "id": 2,
        "name": " ENVIROMENTAL CONFERENCE",
        "date": "04-09-2023",
        "city": " PARIS",
        "attendees": 3000,
    },
    {
        "id": 3,
        "name": "G7 CONFRENCE",
        "date": "20-11-2023",
        "city": "BEIJING",
        "attendees": 10000,
    },
    {
        "id": 4,
        "name": "PEACE BUILDIND SUMMIT",
        "date": "07-10-2024",
        "city": " BUJUMBULA",
        "attendees": 3000,
    },
    {
        "id": 5,
        "name": "YOUTH CONFERENCE",
        "date": "25-12-2023",
        "city": "NAIROBI",
        "attendees": 865,
    }
]

def conference_details(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_details.html', {'conference': conference})

def conference(request):
    return render(request, 'conferences.html', {'conferences': conferences})

def conference_update(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_update.html', {'conference': conference})

def conference_create(request):
    return render(request, 'conference_create.html')

def conference_delete(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_delete.html', {'conference': conference})