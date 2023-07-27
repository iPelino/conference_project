from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "Sandrine Umutoni",
        "date": "2022-04-01",
        "city": "abuja",
        "attendees": 1999,
    },
    {
        "id": 2,
        "name": "patrick kanimba",
        "date": "2022-09-03",
        "city": "nairobi",
        "attendees": 400,
    },
    {
        "id": 3,
        "name": "Diama uwera",
        "date": "2020-08-08",
        "city": "kampala",
        "attendees": 190,
    },
    {
        "id": 4,
        "name": "john kabera",
        "date": "2009-07-01",
        "city": "Dar es salama",
        "attendees": 1300,
    },
    {
        "id": 5,
        "name": "claude kagea",
        "date": "2025-12-01",
        "city": "Kigali",
        "attendees": 2005,
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
