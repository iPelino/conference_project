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



    def Conferences(request):
    data=[
    {
        "id": 1,
        'name': 'Gasabo Conference ',
        'dates': '2023-07-10 to 2023-07-12',
        'location': 'Kigali'
    },
    {
        "id": 2,
        'name': 'Kicukiro Conference ',
        'dates': '2023-08-15 to 2023-08-17',
        'location': 'Kigali'
    },
    {
        "id": 3,
        'name': 'Nyarugenge conference',
        'dates': '2023-09-20 to 2023-09-22',
        'location': 'Kigali'
    },
    
    {
        "id": 4,
        'name': 'Huye Conference',
        'dates': '2023-10-05 to 2023-10-07',
        'location': 'Huye'
    {
        "id": 5,
        'name': 'Gisenyi Conference',
        'dates': '2023-11-12 to 2023-11-14',
        'location': 'Gisenyi'
    }
]
    return render(request,'conference.html',{"data":data})
