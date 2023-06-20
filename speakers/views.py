from django.shortcuts import render

# Create your views here.
speakers = [
        {'name': 'Asaph', 'bio' : 'IT support', 'contact': '0783243222', 'id': 1},
        {'name': 'Mddo', 'bio' : 'IT support', 'contact': '0783243222', 'id': 2},
        {'name': 'Jeth', 'bio' : 'IT support', 'contact': '0783243222', 'id': 3},
        {'name': 'Jenny', 'bio' : 'IT support', 'contact': '0783243222', 'id': 4},
        {'name': 'Josee', 'bio' : 'IT support', 'contact': '0783243222', 'id': 5},
    ]
context = {'speakers': speakers}

def speaker_list(request):
    return render(request, 'speakers/speaker_list.html', context)

def create_speaker(request):
    return(request, 'speakers/create_speaker.html')

def speaker_details(request, speaker_id):
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/speaker_details.html", {"speaker": speaker})
def update_speaker(request, speaker_id):
    # Retrieve speaker information based on speaker_id (dummy data)
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/update_speaker.html", {"speaker": speaker})
def delete_speaker(request, speaker_id):
    
    return render(request, 'speakers/speaker_delete.html')

