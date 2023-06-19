from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "KING BURGER PROMO",
        "date": "2023-05-28",
        "city": "KAMPALA",
        "attendees": 600,
    },
    {
        "id": 2,
        "name": "TOP HIT DANCES",
        "date": "2023-10-01",
        "city": "KIGALI",
        "attendees": 1200,
    },
    {
        "id": 3,
        "name": "INTERNATIONAL Conference",
        "date": "2024-03-01",
        "city": "WARSAW",
        "attendees": 200,
    },
    {
        "id": 4,
        "name": "AFRICAN CHILD",
        "date": "2023-07-11",
        "city": "NAIROBI",
        "attendees": 13500,
    },
    {
        "id": 5,
        "name": "INTERNATIONAL MONETARY FUND",
        "date": "2025-02-01",
        "city": "Zanzibar",
        "attendees": 967,
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