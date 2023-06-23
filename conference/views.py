from django.shortcuts import render
from .models import Conference

conferences = [
    {
        "id": 1,
        "name": "Badget planning",
        "date": "2023-01-01",
        "location": "Lemigo Hotel",
        "title": "Aim tobe Countable"
    },
    {
        "id": 2,
        "name": "BAL",
        "date": "2024-01-01",
        "location": "BK Arena",
        "title": "BAL Preparations"
    },
    {
        "id": 3,
        "name": "CAN",
        "date": "2024-05-21",
        "location": "Huye stadium",
        "title": "pay stadium visit"
    },
    {
        "id": 4,
        "name": "Education",
        "date": "2024-10-08",
        "location": "Serena Hotel",
        "title": "Education For All"
    },
    {
        "id": 5,
        "name": "Miss Rwanda",
        "date": "2025-08-01",
        "location": "Intare Conference Arena",
        "title": "Miss Rwanda BootCamp Compaign"
    }
]
def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})

def conference_create(request):
    return render(request, 'conference_create.html')

def conference_detail(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_detail.html', {'conference': conference})

def conference_update(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_update.html', {'conference': conference})

def conference_delete(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_delete.html', {'conference': conference})
