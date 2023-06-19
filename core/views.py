from django.http import HttpResponse
from django.shortcuts import render


# def home_view(request):
#     data = ['django', 'laravel', 'asp.net core', 'express']
#     return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")

def all_conference_view(request):
    data=[
    {
        "id": 0,
        'name': 'meeting 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'kigali'
    },
    {
        "id": 1,
        'name': 'meeting 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'kigali'
    },
    {
        "id": 2,
        'name': 'meeting 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'kigali'
    },
    {
        "id": 3,
        'name': 'meeting 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'kigali'
    },
    {
        "id": 4,
        'name': 'meeting5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'kigali'
    }
]
    return render(request,'home.html',{"data":data})

def new_conference(request):
    return render(request, 'addconference.html')

def conference_detail(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'meeting 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location A'
    },
    {
        "id": 1,
        'name': 'meeting 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'kigali'
    },
    {
        "id": 2,
        'name': 'meeting 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'kigali'
    },
    {
        "id": 3,
        'name': 'meeting 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'kigali'
    },
    {
        "id": 4,
        'name': 'meeting 5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'kigali'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'conferenceDetail.html',{"data":selectedData})

def update_conference(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'Conference A',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location A'
    },
    {
        "id": 1,
        'name': 'Conference B',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Location B'
    },
    {
        "id": 2,
        'name': 'Conference C',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Location C'
    },
    {
        "id": 3,
        'name': 'Conference D',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Location D'
    },
    {
        "id": 4,
        'name': 'Conference E',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Location E'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, "updateconference.html",{"data":selectedData})

def delete_conference(request,conference_id):
    data=[
    {
        "id": 0,
        'name': 'Meeting1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'kigali'
    },
    {
        "id": 1,
        'name': 'Meeting2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'kigali'
    },
    {
        "id": 2,
        'name': 'Meeting3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'kigali'
    },
    {
        "id": 3,
        'name': 'Meeting4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'kigali'
    },
    {
        "id": 4,
        'name': 'meeting5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'kigali'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'deleteconference.html',{"data":selectedData})


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})