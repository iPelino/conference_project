from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
        {
            "id": 1,
            "name": "Umushyikirino",
            "date": "2023-03-12",
            "location": "kigali convention center"
        },
        {
            "id": 2,
            "name": "CHOGMA",
            "date": "2023-12-12",
            "location": "Bk arena"
        },
        {
            "id": 3,
            "name": "Ndaba event",
            "date": "2023-04-02",
            "location": "mille colline"
        },

        {
            "id": 4,
            "name": "Mbaza nlp",
            "date": "2024-01-01",
            "location": "kivu noir"
        },

        {
            "id": 5,
            "name": "",
            "date": "2024-07-01",
            "location": "BK Arena"
        },
    ]
def conferences_view(request):
    return render(request, 'conference/conferences.html', context={"conferences": conferences})
def create_conference_view(request):
    return render(request, 'createConference.html')
def conference_id(request,id):
    return render(request, 'conferenceId.html')



