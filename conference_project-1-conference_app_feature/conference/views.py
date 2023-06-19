from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "GOA Festival",
        "date": "2023-08-01",
        "city": "Kigali",
        "attendees": 1000,
    },
    {
        "id": 2,
        "name": "Python Hackathon",
        "date": "2023-10-01",
        "city": "Abuja",
        "attendees": 340,
    },
    {
        "id": 3,
        "name": "Django Conference",
        "date": "2024-08-01",
        "city": "Goma",
        "attendees": 14000,
    },
    {
        "id": 4,
        "name": "Youth Connekt",
        "date": "2023-07-01",
        "city": "Addis Ababa",
        "attendees": 13000,
    },
    {
        "id": 5,
        "name": "Transform Africa Summit",
        "date": "2025-08-01",
        "city": "Kigali",
        "attendees": 765,
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