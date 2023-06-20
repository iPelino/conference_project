from django.http import HttpResponse
from django.shortcuts import render


# speakers/views.py


def speaker_list(request):
    # Replace with logic to retrieve a paginated list of speakers
    speakers = [
        {
            'id': 1,
            'name': 'Speaker 1',
            'bio': 'Bio for Speaker 1',
            'contact_info': 'Contact info for Speaker 1',
        },
        # Add dummy speaker data for more speakers
    ]
    context = {'speakers': speakers}
    return render(request, 'speakers/speaker_list.html', context)

def speaker_create(request):
    return render(request, 'speakers/speaker_create.html')

def speaker_detail(request, speaker_id):
    # Replace with logic to retrieve speaker details based on speaker_id
    speaker = {
        'id': speaker_id,
        'name': 'Speaker {}'.format(speaker_id),
        'bio': 'Bio for Speaker {}'.format(speaker_id),
        'contact_info': 'Contact info for Speaker {}'.format(speaker_id),
    }
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_detail.html', context)

def speaker_update(request, speaker_id):
    # Replace with logic to retrieve speaker details based on speaker_id
    speaker = {
        'id': speaker_id,
        'name': 'Speaker {}'.format(speaker_id),
        'bio': 'Bio for Speaker {}'.format(speaker_id),
        'contact_info': 'Contact info for Speaker {}'.format(speaker_id),
    }
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_update.html', context)

def speaker_delete(request, speaker_id):
    # Replace with logic to handle speaker deletion
    speaker = {
        'id': speaker_id,
        'name': 'Speaker {}'.format(speaker_id),
    }
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_delete.html', context)

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