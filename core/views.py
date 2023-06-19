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
