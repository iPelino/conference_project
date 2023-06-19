from django.shortcuts import render
from django.http import HttpResponse

def speakers(request):
    speakers = [
        {'name': 'Jeho', 'bio' : 'IT support', 'contact': '0783243222', 'id': 1},
        {'name': 'Nad', 'bio' : 'IT support', 'contact': '0783243222', 'id': 2},
        {'name': 'John', 'bio' : 'IT support', 'contact': '0783243222', 'id': 3},
        {'name': 'Jenny', 'bio' : 'IT support', 'contact': '0783243222', 'id': 4},
        {'name': 'Jack', 'bio' : 'IT support', 'contact': '0783243222', 'id': 5},
    ]
    return render(request, 'templates/speaker.html', {'speakers': speakers})
def create_speaker(request):
    return render(request, 'template/create_speaker.html')

def speaker_detail(request, speaker_id):
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/speaker_details.html", {"speaker": speaker})
