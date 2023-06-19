from django.shortcuts import render
from django.http import HttpResponse
import datetime

speakers = [
        {
            "id": 1,
            "name": "Introduction to AI",
            "date": "2023-03-12",
            "location": "BK Arena"
        },
        {
            "id": 2,
            "name": "Data Science in health",
            "date": "2023-12-12",
            "location": "Intare Conference Arena"
        },
        {
            "id": 3,
            "name": "Impact of AI on employment",
            "date": "2023-04-02",
            "location": "Hotel Umubano"
        },

        {
            "id": 4,
            "name": "Developing Tech Hubs in Africa",
            "date": "2024-01-01",
            "location": "Intare Conference Arena"
        },

        {
            "id": 5,
            "name": "FIFA Summit 2024",
            "date": "2024-07-01",
            "location": "BK Arena"
        },
    ]
def speakers_view(request):
    return render(request, 'speaker/speakers.html', context={"speaker": speakers})

def create_speaker_view(request):
    return render(request, "speaker/createspeaker.html")

def speaker_view(request,id):
    speaker = None
    for conf in speakers:
        if conf["id"] == int(id):
            speaker = conf
    return render(request, "speaker /speaker .html", context={"speaker ": speaker  })

def update_speaker_view(request,id):
    speaker = None
    for conf in speakers:
        if conf["id"] == int(id):
            speaker = conf
    return render(request, "speaker/updatespeaker.html", context={"speaker ": speaker})

def delete_speaker_view(request,id):
    speaker = None
    for conf in speakers:
        if conf["id"] == int(id):
            speakere = conf
    return render(request, "speaker/delete_speaker.html", context={"speaker" : speaker})

def confirm_delete_view(request, id):
    return render(request, "speaker/confirm_delete.html")