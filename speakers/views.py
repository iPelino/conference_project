from django.shortcuts import render, redirect
from . import speakers_data


def all_speakers(request):
    return render(request, 'speakers/home.html', {'speaker_list': speakers_data.speakers_list})


def create_speaker(request):
    if request.method == 'POST':
        speaker = {
            'name': request.POST.get('name'),
            'address': request.POST.get('address'),
            'bio': request.POST.get('bio'),
        }
        speakers_data.speakers_list.append(speaker)
        return render(request, 'speakers/home.html', {'message': 'New speaker created!'})
    return render(request, 'speakers/create-speaker-form.html')


def view_single_speaker(request, id):
    speaker = None
    for single_speaker in speakers_data.speakers_list:
        if single_speaker["id"] == id:
            speaker = single_speaker
            break
    if speaker:
        data = {'speaker': speaker}
    else:
        data = {'speaker': None}
    return render(request, 'speakers/single_speaker.html', data)


def update_speaker(request, id):
    speaker_to_update = None
    for speaker in speakers_data.speakers_list:
        if speaker['id'] == id:
            speaker_to_update = speaker
            break
    if request.method == "GET":
        return render(request, 'speakers/update-speaker-form.html', {'speaker': speaker_to_update})
    elif request.method == 'POST':
        speaker_to_update['name'] = request.POST.get('name')
        speaker_to_update['address'] = request.POST.get('address')
        speaker_to_update['bio'] = request.POST.get('bio')
        messages.success(request, 'Speaker updated successfully.')
        return redirect('speakers_list')
    messages.error(request, 'Failed to update speaker.')
    return redirect('speakers_list')


def delete_speaker(request, id):
    single_speaker = None
    for speaker in speakers_data.speakers_list:
        if speaker['id'] == id:
            single_speaker = speaker
            break
    if request.method == "POST":
        speakers_data.speakers_list.remove(single_speaker)
        return redirect('speakers_list')
    return render(request, 'speakers/confirmation-page.html', {'speaker': single_speaker})
