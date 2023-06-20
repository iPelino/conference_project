from django.shortcuts import render

# Create your views here.
speakers = [
        {'name': 'Nadia', 'bio' : 'IT support', 'contact': '0783243222', 'id': 1},
        {'name': 'Jim', 'bio' : 'IT support', 'contact': '0783243222', 'id': 2},
        {'name': 'Nadjima', 'bio' : 'IT support', 'contact': '0783243222', 'id': 3},
        {'name': 'John', 'bio' : 'IT support', 'contact': '0783243222', 'id': 4},
        {'name': 'Albertine', 'bio' : 'IT support', 'contact': '0783243222', 'id': 5},
    ]
def speaker_list(request):
    return render(request, 'speakers/speakers_list.html', {'speakers': speakers})
def create_speaker(request):
    return render(request, 'speakers/create_speaker.html')
def speaker_details(request, speaker_id):
    return render(request), 'speakers/speaker_details.html', {'speakers': speakers}    