from django.shortcuts import render
# Create your views here.
conferences = [
        {
       "id": 1,
            "name": "Introduction to AU",
            "date": "2021-07-12",
            "location": "Selena Hotel"
        },
        {
            "id": 2,
            "name": "Meet th President",
            "date": "2023-05-15",
            "location": "Intare Conference Arena"
        },
        {
            "id": 3,
            "name": "Umushyikirano 18",
            "date": "2023-02-27",
            "location": "Gabiro Army Camp"
        },

        {
            "id": 4,
            "name": "Umwiherero 2023",
            "date": "2024-05-0",
            "location": "KCC"
        },

        {
            "id": 5,
            "name": "FIFA Summit 2024",
            "date": "2024-07-01",
            "location": "BK Arena"
            }
    ]
def conferences_available(request):
    return render(request, 'myconferences.html', context={"conferences": conferences})

def new_conference(request):
    return render(request, "conference_creation.html")

def conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "detailsconf.html", context={"conference": conference })

def update_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "updateConf.html", context={"conference": conference})

def delete_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference_removal.html", context={"conference" : conference})

def confirm_delete_view(request, id):
    return render(request, "confirm_deletion.html")