from django.shortcuts import render

# Create your views here.
allspeaker = [
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
def speaker_view(request):
    return render(request, 'allspeakerr.html', context={"speakerr": allspeakerr})

def create_conference_view(request):
    return render(request, 'create_conference.html')

def conference_id(request,id):
    return render(request,'conference_id.html')

def conference_update(request,id):
    return render(request, 'conference_update.html')

def conference_delete(request,id):
    return render(request,'conference_delete.html')



