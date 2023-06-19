from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = [
    {
        "id": 0,
        'first_name': 'james',
        'lastname':'bob',
        'bio':'dr in IT',
        'contact':'8888'
    },
     {
        "id": 1,
        'first_name': 'john',
        'lastname':'mane',
        'bio':'dr in cs',
        'contact':'23343'
    },
     {
        "id": 2,
        'first_name': 'johanna',
        'lastname':'mimi',
        'bio':'dr in is',
        'contact':'23433'
    },
     {
        "id": 3,
        'first_name': 'hanna',
        'lastname':'montan',
        'bio':'exp in biology',
        'contact':'34353'
    },
     {
        "id": 4,
        'first_name': 'justin',
        'lastname':'key',
        'bio':'dr management',
        'contact':'45656'
    },
    ]
    return render(request, 'home.html', {'data': data})

def add(request):

    if request.method=='POST':
       id=request.POST.get('id')
       firstname=request.POST.get('some_value')
       lastname=request.POST.get('id')
       bio=request.POST.get('some_value')
       id=request.POST.get('id')
       


 
def detail(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == id, data))[0]


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})