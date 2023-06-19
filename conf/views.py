from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Speaker
# Create your views here.


speakers=[
        {
            "id":1,
            "name":"oliviertech",
            "bio":"web developer",
            "contact":"tech@gmail"
        }
        ,
        {
            "id":2,
            "name":"oliviertech",
            "bio":"web developer",
            "contact":"tech@gmail"
        },
        {
            "id":3,
            "name":"oliviertech",
            "bio":"web developer",
            "contact":"tech@gmail"
        }
]

def speakers_view(request):
    speaker1=Speaker()
    speaker1.id=1
    speaker1.name="oliviertech"
    speaker1.bio="web developer"
    speaker1.contact="tech@gmail"


    speaker2=Speaker()
    speaker2.id=2
    speaker2.name="olivier"
    speaker2.bio="software engineer"
    speaker2.contact="tech@gmail"


    



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