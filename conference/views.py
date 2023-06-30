from django.shortcuts import render

def conference_list(request):
    conferences = [
        {
            'name': 'Cyusa',
            'dates': '2023-08-18',
            'location': 'Mbiriri',
        },
        {
            'name': 'Grace',
            'dates': '2023-09-20',
            'location': 'Cyugamo',
        },
    ]

    context = {'conferences': conferences}
    return render(request, 'conference/conference_list.html', context)

def conference_create(request):
    return render(request, 'conference/conference_create.html')

def conference_detail(request, conference_id):
    conference = {
        'name': 'Cyusa',
        'dates': '2023-08-18',
        'location': 'Mbiriri',
        'topics': ['cooking', 'machine'],
    }

    context = {'conference': conference}
    return render(request, 'conference/conference_detail.html', context)

def conference_update(request, conference_id):
    conference = {
        'name': 'Grace',
        'dates': '2023-08-15',
        'location': 'Cyugamo',
        'topics': ['president', 'Army'],
    }

    context = {'conference': conference}
    return render(request, 'conference/conference_update.html', context)

def conference_delete(request):
    return render(request, 'conference/conference_delete.html')
