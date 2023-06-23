from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})
def all_conf_view(request):
    data=[
    {
        "id": 000,
        'name': 'conf x',
        'dates': '2024-09-10 to 2024-09-12',
        'location': 'Location x'
    },
    {
        "id": 001,
        'name': 'conf y',
        'dates': '2024-08-15 to 2024-08-19',
        'location': 'Location y'
    },
    {
        "id": 002,
        'name': 'conf z',
        'dates': '2024-09-20 to 2024-09-22',
        'location': 'Location z'
    },
    {
        "id": 003,
        'name': 'conf m',
        'dates': '2024-10-05 to 2024-10-09',
        'location': 'Location m'
    },
    {
        "id": 004,
        'name': 'conf n',
        'dates': '2024-11-12 to 2024-11-14',
        'location': 'Location n'
    }
]
    return render(request,'conf.html',{"data":data})

def new_conf(request):
    return render(request, 'create.html')

def conf_detail(request,conf_id):
    data=[
    {
        "id": 000,
        'name': 'conf x',
        'dates': '2024-09-10 to 2024-09-12',
        'location': 'Location x'
    },
    {
        "id": 001,
        'name': 'conf y',
        'dates': '2024-08-15 to 2024-08-19',
        'location': 'Location y'
    },
    {
        "id": 002,
        'name': 'conf z',
        'dates': '2024-09-20 to 2024-09-22',
        'location': 'Location z'
    },
    {
        "id": 003,
        'name': 'conf m',
        'dates': '2024-10-05 to 2024-10-09',
        'location': 'Location m'
    },
    {
        "id": 004,
        'name': 'conf n',
        'dates': '2024-11-12 to 2024-11-14',
        'location': 'Location n'
    }
]
    for item in data:
        if (item["id"] == conf_id):
            selectedData = item
    return render(request, 'detail.html',{"data":selectedData})

def update_conf(request,conf_id):
    data=[
    {
        "id": 000,
        'name': 'conf x',
        'dates': '2024-09-10 to 2024-09-12',
        'location': 'Location x'
    },
    {
        "id": 001,
        'name': 'conf y',
        'dates': '2024-08-15 to 2024-08-19',
        'location': 'Location y'
    },
    {
        "id": 002,
        'name': 'conf z',
        'dates': '2024-09-20 to 2024-09-22',
        'location': 'Location z'
    },
    {
        "id": 003,
        'name': 'conf m',
        'dates': '2024-10-05 to 2024-10-09',
        'location': 'Location m'
    },
    {
        "id": 004,
        'name': 'conf n',
        'dates': '2024-11-12 to 2024-11-14',
        'location': 'Location n'
    }
]
    for item in data:
        if (item["id"] == conf_id):
            selectedData = item
    return render(request, 'update.html',{"data":selectedData})


def delete_conf(request,conf_id):
    data=[
    {
        "id": 000,
        'name': 'conf x',
        'dates': '2024-09-10 to 2024-09-12',
        'location': 'Location x'
    },
    {
        "id": 001,
        'name': 'conf y',
        'dates': '2024-08-15 to 2024-08-19',
        'location': 'Location y'
    },
    {
        "id": 002,
        'name': 'conf z',
        'dates': '2024-09-20 to 2024-09-22',
        'location': 'Location z'
    },
    {
        "id": 003,
        'name': 'conf m',
        'dates': '2024-10-05 to 2024-10-09',
        'location': 'Location m'
    },
    {
        "id": 004,
        'name': 'conf n',
        'dates': '2024-11-12 to 2024-11-14',
        'location': 'Location n'
    }
]
    for item in data:
        if (item["id"] == conf_id):
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