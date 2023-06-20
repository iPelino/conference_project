from django.shortcuts import render

# Create your views here.
speakers = [
        {'name': 'Jeho', 'bio' : 'IT support', 'contact': '0783243222', 'id': 1},
        {'name': 'Nad', 'bio' : 'IT support', 'contact': '0783243222', 'id': 2},
        {'name': 'John', 'bio' : 'IT support', 'contact': '0783243222', 'id': 3},
        {'name': 'Jenny', 'bio' : 'IT support', 'contact': '0783243222', 'id': 4},
        {'name': 'Jack', 'bio' : 'IT support', 'contact': '0783243222', 'id': 5},
    ]
context = {'speakers': speakers}

def speaker_list(request):
    return render(request, 'speakers/speaker_list.html', context)
