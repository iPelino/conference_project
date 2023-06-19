from django.shortcuts import render, redirect
from django.http import HttpResponse

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
    try:
        conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
        return render(request, 'conference_details.html', {'conference': conference})
    except IndexError:
        return render(request, 'conference_not_found.html')

def conference(request):
    return render(request, 'conferences.html', {'conferences': conferences})

def conference_update(request, conference_id: int):
    try:
        conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
        return render(request, 'conference_update.html', {'conference': conference})
    except IndexError:
        return render(request, 'conference_not_found.html')

def conference_update_confirm(request, conference_id: int):
    try:
        if (request.method == 'POST'):
            conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
            conference['name'] = request.POST['name']
            conference['date'] = request.POST['date']
            conference['city'] = request.POST['city']
            conference['attendees'] = request.POST['attendees']
            return redirect(f'/conferences/{conference_id}', {'conference': conference})
        return render(request, 'conferences.html', {'conferences': conferences})
    except IndexError:
        return render(request, 'conference_not_found.html')

def conference_create(request):
    return render(request, 'conference_create.html')

def conference_delete(request, conference_id: int):
    try:
        conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
        return render(request, 'conference_delete.html', {'conference': conference})
    except IndexError:
        return render(request, 'conference_not_found.html')

def conference_delete_confirm(request, conference_id: int):
    if (request.method == 'POST'):
        conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
        conferences.remove(conference)
        return redirect('conferences')
    return render(request, 'conferences.html', {'conferences': conferences})