from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})

from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")

    def new_conference(request):
    return render(request, 'create.html')

def detail_conference(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'Conference 1',
        'dates': '2020-08-11 ',
        'location': 'Place 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2020-09-16',
        'location': 'Place 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2020-10-21 ',
        'location': 'Place 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2020-11-06',
        'location': 'Place 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2020-12-13 ',
        'location': 'Place 5'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'detail.html',{"data":selectedData})

def update_conference(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'Conference 1',
        'dates': '2020-08-11',
        'location': 'Place 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2020-09-16',
        'location': 'Place 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2020-10-21',
        'location': 'Place 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2020-11-06',
        'location': 'Place 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2020-12-13',
        'location': 'Place 5'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'update.html',{"data":selectedData})


def delete_conference(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'Conference A',
        'dates': '2023-07-10',
        'location': 'Location A'
    },
    {
        "id": 1,
        'name': 'Conference B',
        'dates': '2023-08-15',
        'location': 'Location B'
    },
    {
        "id": 2,
        'name': 'Conference C',
        'dates': '2023-09-20',
        'location': 'Location C'
    },
    {
        "id": 3,
        'name': 'Conference D',
        'dates': '2023-10-05',
        'location': 'Location D'
    },
    {
        "id": 4,
        'name': 'Conference E',
        'dates': '2023-11-12',
        'location': 'Location E'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'delete.html',{"data":selectedData})



def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})
def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})