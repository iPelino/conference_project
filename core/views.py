from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def speakers_view(request):
    data = [
        {
        "id": 0,
        'name': 'Speaker Waze',
        'bios': '11/03/2000',
        'location': 'Kiramuruzi'
    },
    {
        "id": 1,
        'name': 'Speaker byuku',
        'bios': '23/9/1995',
        'location': 'Kiyovu'
    },
    {
        "id": 2,
        'name': 'Speaker mugisha',
        'bios': '8/12/2003',
        'location': 'Gisenyi'
    },
    {
        "id": 3,
        'name': 'Speaker mugisha',
        'bios': '12/12/2000',
        'location': 'Muhanga'
    },
    {
        "id": 4,
        'name': 'Speaker Hipla',
        'bios': '1/1/1988',
        'location': 'Kibagabaga'
    }
    ]
    return render(request,'speakers.html',{"data":data})

def create(request):
    return render(request, 'create.html')

def speakers_details(request,speaker_id):
    data = [
        {
        "id": 0,
        'name': 'Speaker Waze',
        'bios': '11/03/2000',
        'location': 'Kiramuruzi'
    },
    {
        "id": 1,
        'name': 'Speaker byuku',
        'bios': '23/9/1995',
        'location': 'Kiyovu'
    },
    {
        "id": 2,
        'name': 'Speaker mugisha',
        'bios': '8/12/2003',
        'location': 'Gisenyi'
    },
    {
        "id": 3,
        'name': 'Speaker mugisha',
        'bios': '12/12/2000',
        'location': 'Muhanga'
    },
    {
        "id": 4,
        'name': 'Speaker Hipla',
        'bios': '1/1/1988',
        'location': 'Kibagabaga'
    }   
    ]
    for item in data:
        if (item["id"] == speaker_id):
            selectedData=item
    return render(request, 'speaker_details.html',{"data":selectedData})

def update_speaker(request,speaker_id):
    data= [
    {
        "id": 0,
        'name': 'Speaker Waze',
        'bios': '11/03/2000',
        'location': 'Kiramuruzi'
    },
    {
        "id": 1,
        'name': 'Speaker byuku',
        'bios': '23/9/1995',
        'location': 'Kiyovu'
    },
    {
        "id": 2,
        'name': 'Speaker mugisha',
        'bios': '8/12/2003',
        'location': 'Gisenyi'
    },
    {
        "id": 3,
        'name': 'Speaker mugisha',
        'bios': '12/12/2000',
        'location': 'Muhanga'
    },
    {
        "id": 4,
        'name': 'Speaker Hipla',
        'bios': '1/1/1988',
        'location': 'Kibagabaga'
    }
    ]
    for item in data:
        if (item["id"] == speaker_id):
            selectedData = item
    return render(request, 'update.html',{"data":selectedData})

def delete_speaker(request,speaker_id):
    data= [
    {
        "id": 0,
        'name': 'Speaker Waze',
        'bios': '11/03/2000',
        'location': 'Kiramuruzi'
    },
    {
        "id": 1,
        'name': 'Speaker byuku',
        'bios': '23/9/1995',
        'location': 'Kiyovu'
    },
    {
        "id": 2,
        'name': 'Speaker mugisha',
        'bios': '8/12/2003',
        'location': 'Gisenyi'
    },
    {
        "id": 3,
        'name': 'Speaker mugisha',
        'bios': '12/12/2000',
        'location': 'Muhanga'
    },
    {
        "id": 4,
        'name': 'Speaker Hipla',
        'bios': '1/1/1988',
        'location': 'Kibagabaga'
    } 
    ] 
    for item in data:
        if (item["id"] == speaker_id):
            selectedData = item
    return render(request, 'delete_speaker.html',{"data":selectedData})

def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})