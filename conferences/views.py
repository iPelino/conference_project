from django.shortcuts import render
# Create your views here.
conferences = [
        {
            "id": 1,
            "name": "glance",
            "date": "2023-05-4",
            "location": "convetion center"
        },
        {
            "id": 2,
            "name": "health",
            "date": "2023-5-17",
            "location": "blablaq"
        },
        {
            "id": 3,
            "name": "data collection",
            "date": "2023-07-24",
            "location": "kigali view"
        },

        {
            "id": 4,
            "name": "home of people",
            "date": "2023-08-02",
            "location": "splendid hotel"
        },

        {
            "id": 5,
            "name": "tourism",
            "date": "2024-08-31",
            "location": "fantastica"
        },
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