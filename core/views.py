from django.http import HttpResponse
from django.shortcuts import render


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

def conference_list(request):
    data=[
    {
        "id": 0,
        'name': 'Conference 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Location 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Location 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Location 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Location 5'
    }
]
    return render(request,'conference_view.html',{"data":data})

def conference(request):
    return render(request, 'create_conference.html')

def conference_detail(request,conference_id):
    data=[
     {
        "id": 0,
        'name': 'Conference 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Location 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Location 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Location 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Location 5'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'delete.html',{"data":selectedData})
def update_conference(request,conference_id):
    data=[
     {
        "id": 0,
        'name': 'Conference 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Location 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Location 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Location 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Location 5'
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
        'name': 'Conference 1',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Location 1'
    },
    {
        "id": 1,
        'name': 'Conference 2',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Location 2'
    },
    {
        "id": 2,
        'name': 'Conference 3',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Location 3'
    },
    {
        "id": 3,
        'name': 'Conference 4',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Location 4'
    },
    {
        "id": 4,
        'name': 'Conference 5',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Location 5'
    }
]
    for item in data:
        if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'delete.html',{"data":selectedData})




def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})
