from django.http import HttpResponse
from django.shortcuts import render

def conference_list(request):
    conferences = [
        {
            'id': 0,
            'name': 'Conference A',
            'dates': 'June 1-3, 2023',
            'location': 'City V',
        },
        {
            'id': 1,
            'name': 'Conference B',
            'dates': 'July 10-12, 2023',
            'location': 'City W',
        },
        {
            'id': 2,
            'name': 'Conference C',
            'dates': 'August 5-7, 2023',
            'location': 'City X',
        },
        {
            'id': 3,
            'name': 'Conference D',
            'dates': 'August 5-7, 2023',
            'location': 'City Y',
        },
        {
            'id': 4,
            'name': 'Conference E',
            'dates': 'August 5-7, 2023',
            'location': 'City Z',
        },
    ]
    context = {
        'conferences': conferences
    }
    return render(request, 'conference/conference_list.html', context)

def create_conference(request):
    return render(request, 'conference/create_conference.html')

def conference_details(request, conference_id):
    conference = {
        'id': conference_id,
        'name': 'Conference A',
        'dates': 'June 1-3, 2023',
        'location': 'City X',
        'topics': 'Topic 1, Topic 2, Topic 3',
        'description': 'This is a detailed description of Conference A.',
    }
    context = {
        'conference': conference
    }
    return render(request, 'conference/conference_details.html', context)

def update_conference(request, conference_id):
    conference = {
        'id': conference_id,
        'name': 'Conference A',
        'dates': 'June 1-3, 2023',
        'location': 'City X',
        'topics': 'Topic 1, Topic 2, Topic 3',
        'description': 'This is a detailed description of Conference A.',
    }
    context = {
        'conference': conference
    }
    return render(request, 'conference/update_conference.html', context)

def delete_conference(request, conference_id):
    conference = {
        'id': conference_id,
        'name': 'Conference A',
        'dates': 'June 1-3, 2023',
        'location': 'City X',
        'topics': 'Topic 1, Topic 2, Topic 3',
        'description': 'This is a detailed description of Conference A.',
    }
    context = {
        'conference': conference
    }
    return render(request, 'conference/delete_conference.html', context)


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
