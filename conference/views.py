from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "Festival",
        "date": "2023-08-01",
        "city": "kampala",
        "attendees": 900,
    },
    {
        "id": 2,
        "name": "AZAM TRAINNING",
        "date": "2023-10-01",
        "city": "KIGALI",
        "attendees": 3540,
    },
    {
        "id": 3,
        "name": "WN CONFRENCE",
        "date": "2024-08-01",
        "city": "MOMBASA",
        "attendees": 1670,
    },
    {
        "id": 4,
        "name": "YOUTH VOLONTEER",
        "date": "2023-07-01",
        "city": "MWENDENI",
        "attendees": 568,
    },
    {
        "id": 5,
        "name": "Transforming Africa",
        "date": "2025-08-01",
        "city": "NIGERI",
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