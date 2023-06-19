from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


speakers=[
    {
        "id": 1,
        "name": "hopesmith",
        "bio": "software engineer",
        "contact": "john.smith@gmail.com"
    },
    {
        "id": 2,
        "name": "jenniferwhite",
        "bio": "UI/UX designer",
        "contact": "jennifer.white@gmail.com"
    },
    {
        "id": 3,
        "name": "davidmiller",
        "bio": "data scientist",
        "contact": "david.miller@gmail.com"
    },
    {
        "id": 4,
        "name": "enockteck",
        "bio": "frontend developer",
        "contact": "emily.brown@gmail.com"
    },
    {
        "id": 5,
        "name": "alexanderjones",
        "bio": "backend developer",
        "contact": "alexander.jones@gmail.com"
    }
]

def speakers_view(request):
   


    return render(request, 'speakers.html',{"speakers":speakers})

def create(request):
    return render(request, 'createspeaker.html')



def speaker(request,id):
    sp = None
    print(speakers)
    for speak in speakers:
        if speak["id"] == int(id):
        # if speak.id == int(id):
            sp = speak
    return render(request, 'speaker.html',{"speaker":sp})