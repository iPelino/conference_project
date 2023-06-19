from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "YOUTH IMPACTconference",
        "date": "2023-07-04",
        "city": "Kigali",
        "attendees": 2000,
    },
    {
        "id": 2,
        "name": "COGAM ",
        "date": "2023-09-54",
        "city": "cairo",
        "attendees": 500,
    },
    {
        "id": 3,
        "name": "GOLDBACKK",
        "date": "2024-07-01",
        "city": "BERLIN",
        "attendees": 2300,
    },
    {
        "id": 4,
        "name": "UMUSHYIKIRANO",
        "date": "2023-04-03",
        "city": "KAMPALA",
        "attendees": 1340,
    },
    {
        "id": 5,
        "name": "ghael ghana",
        "date": "2025-10-09",
        "city": "Kampala",
        "attendees": 350,
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