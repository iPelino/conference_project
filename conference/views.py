from django.shortcuts import render

conferences = [
        {
            "id": 1,
            "name": "Gils in ICT",
            "date": "2023-03-12",
            "location": "CcHUB"
        },
        {
            "id": 2,
            "name": "Introduction to AI",
            "date": "2023-12-12",
            "location": "BK Arena"
        },
        {
            "id": 3,
            "name": "Impact of AI on employment",
            "date": "2023-04-02",
            "location": "Lemigo Hotel"
        },

        {
            "id": 4,
            "name": "Developing Tech in Rwanda",
            "date": "2024-01-01",
            "location": "Intare Conference Arena"
        },

        {
            "id": 5,
            "name": "Women in Tech",
            "date": "2024-07-01",
            "location": "Radisson Hotel"
        },
    ]
def conferences_list(request):
    return render(request,'dataconference.html' ,context={"conferences": conferences})

def create_new_conference(request):
    return render(request, "new_conference.html")

def conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conf_detail.html", context={"conference": conference })
