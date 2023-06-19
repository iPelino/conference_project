from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})

speakers_data = [
    {
        'id': 1,
        'name': 'John Doe',
        'bio': 'John Doe is a software engineer with expertise in web development.',
        'contact': 'john.doe@example.com',
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'bio': 'Jane Smith is a data scientist specializing in machine learning.',
        'contact': 'jane.smith@example.com',
    },

]
def speaker_list(request):
    # Paginated list of speakers
    speakers = speakers_data
    context = {'speakers': speakers}
    return render(request, 'speakers/speaker_list.html', context)

def create_speaker(request):
    # Form to create a new speaker
    return render(request, 'speakers/create_speaker.html')

def speaker_details(request, speaker_id):
    # Details of a specific speaker
    speaker = next((speaker for speaker in speakers_data
    if speaker['id'] == int(speaker_id)), None)
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_details.html', context)

def update_speaker(request, speaker_id):
    # Form to update a specific speaker
    speaker = next((speaker for speaker in speakers_data
    if speaker['id'] == int(speaker_id)), None)
    context = {'speaker': speaker}
    return render(request, 'speakers/update_speaker.html', context)

def delete_speaker(request, speaker_id):
    # Form to delete a specific speaker
    speaker = next((speaker for speaker in speakers_data
    if speaker['id'] == int(speaker_id)), None)
    context = {'speaker': speaker}
    return render(request, 'speakers/delete_speaker.html', context)