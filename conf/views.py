from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Speaker
# Create your views here.



def speakers(request):
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


    


    speakers=[speaker1,speaker2]

    return render(request, 'speakers.html',{"speakers":speakers})
