from django.shortcuts import render, redirect

conferances = {
        1: {
            'name': 'Chogam',
            'date': '12/12/2022',
            'location': 'kcc'
        },
        2: {
            'name': 'Tech expart',
            'date': '02/12/2022',
            'location': 'Muhazi'
        },
        3: {
            'name': 'Youth conference',
            'date': '03/03/2021',
            'location': 'Muhabura'
        },
        4: {
            'name': 'Fifa conference',
            'date': '08/12/2022',
            'location': 'Camp kigali'
        },
        5: {
            'name': 'fiba',
            'bio': '03/23/2023',
            'location': 'Bk arena'
        },
    }


def list_of_conference(request):
	

	
	context = {'conferences': conferences}
	return render(request, 'conference/conferences.html', context)

def conference_create(request):
    

    return render(request, 'conference/register.html')


def conference_detail(request, id):
    conferances = {
        1: {
            'name': 'Chogam',
            'date': '12/12/2022',
            'location': 'kcc'
        },
        2: {
            'name': 'Tech expart',
            'date': '02/12/2022',
            'location': 'Muhazi'
        },
        3: {
            'name': 'Youth conference',
            'date': '03/03/2021',
            'location': 'Muhabura'
        },
        4: {
            'name': 'Fifa conference',
            'date': '08/12/2022',
            'location': 'Camp kigali'
        },
        5: {
            'name': 'fiba',
            'bio': '03/23/2023',
            'location': 'Bk arena'
        },
    }
    conference = conferences.get(int(id))
    return render(request, 'conference/detail.html', {'conference': conference})


def conference_update(request, id):
    conferances = {
        1: {
            'name': 'Chogam',
            'date': '12/12/2022',
            'location': 'kcc'
        },
        2: {
            'name': 'Tech expart',
            'date': '02/12/2022',
            'location': 'Muhazi'
        },
        3: {
            'name': 'Youth conference',
            'date': '03/03/2021',
            'location': 'Muhabura'
        },
        4: {
            'name': 'Fifa conference',
            'date': '08/12/2022',
            'location': 'Camp kigali'
        },
        5: {
            'name': 'fiba',
            'bio': '03/23/2023',
            'location': 'Bk arena'
        },
    }


    conference = conferences.get(int(id))

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        location = request.POST.get('location')
        # Update the speaker details in the dictionary
        conferences['name'] = name
        conferences['date'] = date
        conferences['location'] = location
        return redirect('conference_detail', id=id)

    return render(request, 'conference/update.html', {'conference': conference})



def conferance_delete(request, id):
    conferances = {
        1: {
            'name': 'Chogam',
            'date': '12/12/2022',
            'location': 'kcc'
        },
        2: {
            'name': 'Tech expart',
            'date': '02/12/2022',
            'location': 'Muhazi'
        },
        3: {
            'name': 'Youth conference',
            'date': '03/03/2021',
            'location': 'Muhabura'
        },
        4: {
            'name': 'Fifa conference',
            'date': '08/12/2022',
            'location': 'Camp kigali'
        },
        5: {
            'name': 'fiba',
            'bio': '03/23/2023',
            'location': 'Bk arena'
        },
    }

    conference = conferences.get(int(id))
    return render(request, 'conferences/delete.html', {'conferance': conference})

