from django.shortcuts import render


def speaker_list(request):
    speakers = [
        {"id": 1, "name": "Speaker1", "bio": "Bio1", "address": "address1"},
        {"id": 2, "name": "Speaker2", "bio": "Bio2", "address": "address2"},
        {"id": 3, "name": "Speaker3", "bio": "Bio3", "address": "address3"},
        {"id": 4, "name": "Speaker4", "bio": "Bio4", "address": "address4"},
        {"id": 5, "name": "Speaker5", "bio": "Bio5", "address": "address5"},
    ]
    return render(request, "speakers/speaker_list.html", {"speakers": speakers})


def create_speaker(request):
    return render(request, 'speakers/create_speaker.html')


def speaker_details(request, speaker_id):
    # Retrieve speaker information based on speaker_id (dummy data)
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/speaker_details.html", {"speaker": speaker})

