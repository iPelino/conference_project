from django.shortcuts import render

# Create your views here.
def speaker_list(request):
    # Dummy static speaker data
    speakers = [
        {"id": 1, "name": "Speaker 1", "bio": "Speaker 1 bio"},
        {"id": 2, "name": "Speaker 2", "bio": "Speaker 2 bio"},
        # Add more dummy speaker data
    ]
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})

