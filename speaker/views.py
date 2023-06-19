from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

speakers = [
        {
            "id": 1,
            "name": "Eric Ndungutse",
            "birthdate": "1996-03-12",
            "country": "Rwanda",
            "email":"eric@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },
        {
            "id": 2,
            "name": "James Mugabo",
            "birthdate": "1996-12-12",
            "country": "Rwanda",
            "email":"james@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },
        {
            "id": 3,
            "name": "Alice Uwera",
            "birthdate": "1996-04-02",
            "country": "Rwanda",
            "email":"alice@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },

        {
            "id": 4,
            "name": "Patrick Ngabo",
            "birthdate": "1999-01-01",
            "country": "Rwanda",
            "email":"patrick@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },

        {
            "id": 5,
            "name": "Silas Nizeye",
            "birthdate": "1999-07-01",
            "country": "Rwanda",
            "email":"silas@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },
    ]

def speakers_view(request):
    return render(request, 'speakers/speakers.html', context={"speakers": speakers})

def create_speaker_view(request):
    return render(request, "speakers/createSpeaker.html")

def speaker_view(request,id):
    speaker = None
    for spek in speakers:
        if spek["id"] == int(id):
            speaker = spek
    return render(request, "speakers/speaker.html", context={"speaker": speaker })

def update_speaker_view(request,id):
    speaker = None
    for spek in speakers:
        if spek["id"] == int(id):
            speaker = spek
    return render(request, "speakers/updateSpeaker.html", context={"speaker": speaker})

def delete_speaker_view(request,id):
    speaker = None
    for spek in speakers:
        if spek["id"] == int(id):
            speaker = spek
    return render(request, "speakers/delete_speaker.html", context={"speaker" : speaker})

def confirm_delete_view(request, id):
    return render(request, "speakers/confirm_delete.html")