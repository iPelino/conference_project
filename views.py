from django.shortcuts import render

conferences = [
    {
        'id':1,
        "name": "InterPol Peace Keeping Conference",
        "date": "2023-12-01",
        "location": "Musanze, Rwanda"
    },
    {
        'id':2,
        "name": "East African General Meeting",
        "date": "2023-11-05",
        "location": "Kigali, Rwanda"
    },
    {
        'id':3,
        "name": "International Malaria Yearly Conference",
        "date": "2023-09-09",
        "location": "Amsterdam, Netherlands"
    },
    {
        'id':4,
        "name": "National Liberation Day Celebration",
        "date": "2023-07-04",
        "location": "Kigali, Rwanda"
    {
        'id':5,
         "name": "National Umushyikirano",
        "date": "2023-12-03",
        "location": "Kigali, Rwanda"
    },
    {
        'id':6,
        'name': 'PyCon France',
        'city': 'Paris',
        'country': 'France',
        'date': '2021-10-08',
        'url': 'https://www.pycon.fr/'
    }
]




def home(request):
    return render(request, 'conferences.html', {'conferences': conferences})


def single_conference(request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    return render(request, 'single_conference.html', {'conference': conference})

def update_conference(request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    name = request.POST.get('name')
    city = request.POST.get('city')
    country = request.POST.get('country')
    conference['name'] = name
    conference['city'] = city
    conference['country'] = country
    return render(request, 'update_conference.html', {'conference': conference})

def delete_confrence(request, id: int):
    conference = list(filter(lambda c: c['id'] == id, conferences))[0]
    conferences.remove(conference)
    return render(request, 'conferences.html', {'conferences': conferences})

def create_conference(request):
    return render(request, 'create_conference.html')