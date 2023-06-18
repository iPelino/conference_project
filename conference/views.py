from django.shortcuts import render
from django.http import HttpResponse


def conferences_view(request):
    # name, dates, and location
    conferences = [
        {
            "name": "Introduction to AI",
            "date": "2023-03-12",
            "location": "BK Arena"
        },
        {
            "name": "Data Science in health",
            "date": "2023-12-12",
            "location": "Intare Conference Arena"
        },
        {
            "name": "Impact of AI on employment",
            "date": "2023-04-02",
            "location": "Hotel Umubano"
        },

        {
            "name": "Developing Tech Hubs in Africa",
            "date": "2024-01-01",
            "location": "Intare Conference Arena"
        },

        {
            "name": "FIFA Summit 2024",
            "date": "2024-07-01",
            "location": "BK Arena"
        },
    ]

    return render(request, 'conference/conferences.html', context={"conferences": conferences})

def create_conference_view(request):
    return render(request, "conference/createConference.html")