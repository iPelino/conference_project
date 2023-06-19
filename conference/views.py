from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "Africa Soft Summit",
        "date": "2023-12-01",
        "city": "Cairo",
        "attendees": 1000,
    },
    {
        "id": 2,
        "name": "Finetech Foum",
        "date": "2023-12-05",
        "city": "Dakar",
        "attendees": 34340,
    },
    {
        "id": 3,
        "name": "BillGte golf day",
        "date": "2023-12-23",
        "city": "Boston",
        "attendees": 14000,
    },
    {
        "id": 4,
        "name": "Norrsken Summit",
        "date": "2023-11-01",
        "city": "New York",
        "attendees": 13500,
    },
    {
        "id": 5,
        "name": "Peak History day",
        "date": "2025-08-02",
        "city": "Kigali",
        "attendees": 1500,
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