from django.shortcuts import render

# Create your views here.
# speakers/views.py

from django.shortcuts import render, get_object_or_404
from speakers.models import Speaker



def speaker_list(request):
    speakers = Speaker.objects.all()  # Retrieve all speakers
    context = {'speakers': speakers}
    return render(request, 'speakers/speaker_list.html', context)

def speaker_create(request):
    # Render the form to create a new speaker
    return render(request, 'speakers/speaker_create.html')

def speaker_detail(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)  # Retrieve the specific speaker
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_detail.html', context)

def speaker_update(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)  # Retrieve the specific speaker
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_update.html', context)

def speaker_delete(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)  # Retrieve the specific speaker
    context = {'speaker': speaker}
    return render(request, 'speakers/speaker_delete.html', context)

     
    