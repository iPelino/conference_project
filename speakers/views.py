from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Speaker

#create views here

def speakers_list(request):
    speakers = [
        {'id': 1, 'name': 'Speaker 1', 'bio': 'Speaker 1 bio', 'location': 'City A'},
        {'id': 2, 'name': 'Speaker 2', 'bio': 'Speaker 2 bio', 'location': 'City B'},
        {'id': 3, 'name': 'Speaker 3', 'bio': 'Speaker 3 bio', 'location': 'City C'},
        {'id': 4, 'name': 'Speaker 4', 'bio': 'Speaker 4 bio', 'location': 'City D'},
        {'id': 5, 'name': 'Speaker 5', 'bio': 'Speaker 5 bio', 'location': 'City E'},
        # Add more dummy speaker information
    ]
    return render(request, 'speakers/speakers_list.html', {'speakers': speakers})


def speaker_create(request):
    return render(request, 'speakers/speaker_create.html')

def speaker_detail(request, speaker_id):
    speakers = [
        {'id': 1, 'name': 'Speaker 1', 'bio': 'Speaker bio 1', 'contact': 'speaker1@example.com'},
        {'id': 2, 'name': 'Speaker 2', 'bio': 'Speaker bio 2', 'contact': 'speaker2@example.com'},
        {'id': 3, 'name': 'Speaker 3', 'bio': 'Speaker bio 3', 'contact': 'speaker3@example.com'},
        {'id': 4, 'name': 'Speaker 4', 'bio': 'Speaker bio 4', 'contact': 'speaker4@example.com'},
        {'id': 5, 'name': 'Speaker 5', 'bio': 'Speaker bio 5', 'contact': 'speaker5@example.com'},
    ]

    speaker = None
    for spk in speakers:
        if spk['id'] == speaker_id:
            speaker = spk
            break

    if speaker is None:
        raise Http404("Speaker does not exist.")

    return render(request, 'speakers/speaker_detail.html', {'speaker': speaker})

def speaker_update(request, speaker_id):
    speaker = {'name': 'Speaker 1', 'bio': 'Dummy Bio', 'contact': 'Dummy Contact Info'}
    return render(request, 'speakers/speaker_update.html', {'speaker': speaker})

def speaker_delete(request, speaker_id):
    return render(request, 'speakers/speaker_delete.html')
