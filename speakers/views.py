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
