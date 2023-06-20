from django.shortcuts import render

# Create your views here.
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
    {
        'id': 3,
        'name': 'peter',
        'bio': 'xxxxxxxxxxxxxxxxxxxxxxxx.',
        'contact': 'xxx@example.com',
    },
    {
        'id': 4,
        'name': 'Jo.Smith',
        'bio': 'Jo is the best dancer ever.',
        'contact': 'jo@example.com',
    },
    {
        'id': 5,
        'name': 'Jonathan muyoya',
        'bio': '      .',
        'contact': 'youandme@example.com',
    },

]


def speaker_list(request):
    conferences = Conference.objects.all()[:5]  # Assuming you have a Conference model
    return render(request, 'speaker_list.html', {'speaker': speaker}
def update_speaker(request, speaker_id):
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/update speaker.html", {"speaker": speaker})

def delete_speaker(request, speaker_id):
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, 'speakers/speaker_delete.html', {"speaker": speaker})