from django.shortcuts import render, redirect

speakers = {
    1:{
        	
            'name': 'Benitha',
            'bio': 'Developer 1',
            'other_info':'Developer'
        },
        2:{
            'name': 'Rosine',
            'bio': 'Developer 2',
            'other_info':'Developer'
        },
        3:{
            'name': 'Sandrine',
            'bio': 'Developer 3',
            'other_info':'Developer'
        },
        4:{
            'name': 'David',
            'bio': 'Developer 4',
            'other_info':'Developer'
        },
        5:{
            'name': 'Nadege',
            'bio': 'Developer 5',
            'other_info':'Developer'
        },
    }
        





def list_of_speaker(request):
	

	
	context = {'speakers': speakers}
	return render(request, 'speaker/speakers.html', context)

def speaker_create(request):
    

    return render(request, 'speaker/register.html')


def speaker_detail(request, id):
    speakers = {
        1: {
            'name': 'Benitha',
            'bio': 'Developer 1',
            'other_info': 'Developer'
        },
        2: {
            'name': 'Rosine',
            'bio': 'Developer 2',
            'other_info': 'Developer'
        },
        3: {
            'name': 'Sandrine',
            'bio': 'Developer 3',
            'other_info': 'Developer'
        },
        4: {
            'name': 'David',
            'bio': 'Developer 4',
            'other_info': 'Developer'
        },
        5: {
            'name': 'Nadege',
            'bio': 'Developer 5',
            'other_info': 'Developer'
        },
    }

    speaker = speakers.get(int(id))
    return render(request, 'speaker/detail.html', {'speaker': speaker})


def speaker_update(request, id):
    speakers = {
        1: {
            'name': 'Benitha',
            'bio': 'Developer 1',
            'other_info': 'Developer'
        },
        2: {
            'name': 'Rosine',
            'bio': 'Developer 2',
            'other_info': 'Developer'
        },
        3: {
            'name': 'Sandrine',
            'bio': 'Developer 3',
            'other_info': 'Developer'
        },
        4: {
            'name': 'David',
            'bio': 'Developer 4',
            'other_info': 'Developer'
        },
        5: {
            'name': 'Nadege',
            'bio': 'Developer 5',
            'other_info': 'Developer'
        },
    }


    speaker = speakers.get(int(id))

    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        other_info = request.POST.get('other_info')
        # Update the speaker details in the dictionary
        speaker['name'] = name
        speaker['bio'] = bio
        speaker['other_info'] = other_info
        return redirect('speaker_detail', id=id)

    return render(request, 'speaker/update.html', {'speaker': speaker})



def speaker_delete(request, id):
    speakers = {
        1: {
            'name': 'Benitha',
            'bio': 'Developer 1',
            'other_info': 'Developer'
        },
        2: {
            'name': 'Rosine',
            'bio': 'Developer 2',
            'other_info': 'Developer'
        },
        3: {
            'name': 'Sandrine',
            'bio': 'Developer 3',
            'other_info': 'Developer'
        },
        4: {
            'name': 'David',
            'bio': 'Developer 4',
            'other_info': 'Developer'
        },
        5: {
            'name': 'Nadege',
            'bio': 'Developer 5',
            'other_info': 'Developer'
        },
    }

    speaker = speakers.get(int(id))
    return render(request, 'speaker/delete.html', {'speaker': speaker})

