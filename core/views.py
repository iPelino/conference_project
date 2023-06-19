from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = [
        {
            'name': 'Conference 1',
            'dates': 'October 1-3, 2023',
            'location': 'Rusizi',
        },
        {
            'name': 'Conference 2',
            'dates': 'November 5-7, 2023',
            'location': 'Gasabo',
        },
        {
            'name': 'Conference 3',
            'dates': 'December 10-12, 2023',
            'location': 'Kirehe',
        },
        {
            'name': 'Conference 4',
            'dates': 'January 15-17, 2024',
            'location': 'Gisozi',
        },
        {
            'name': 'Conference 5',
            'dates': 'February 20-22, 2024',
            'location': 'Kabuga',
        },
    ]
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
