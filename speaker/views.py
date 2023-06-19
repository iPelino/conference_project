from django.shortcuts import render

speaker = [
        {
            "id": 1,
            "name": "Ngoga Jovin",
            "birthdate": "2000-03-12",
            "country": "Rwanda",
            "email":"eric@example.com",
            "bio":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        },
        {
            "id": 2,
            "name": "Inkora Jane",
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
    return render(request, 'biography.html', context={"speakers": speaker  })

def create_speaker_view(request):
    return render(request, "create_form.html")

def speaker_view(request,id):
    speaker = None
    for info in speaker :
        if info["id"] == int(id):
            speaker = info
    return render(request, "biography.html", context={"speaker": speaker })

def update_speaker_view(request,id):
    speaker = None
    for info in speaker :
        if info["id"] == int(id):
            speaker = info
    return render(request, "update_form.html", context={"speaker": speaker})

def delete_speaker_view(request,id):
    speaker = None
    for info in speaker :
        if info["id"] == int(id):
            speaker = info
    return render(request, "delete_form.html", context={"speaker" : speaker})

def confirm_delete_view(request, id):
    return render(request, "delete.html")
