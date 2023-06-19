from django.shortcuts import render

conferences = [
    {
        'id':1,
        'name': 'PyCon India',
        'city': 'Hyderabad',
        'country': 'India',
        'date': '2021-09-25',
        'url': 'https://in.pycon.org/2021/'
    },
    {
        'id':2,
        'name': 'PyCon US',
        'city': 'Pittsburgh',
        'country': 'USA',
        'date': '2021-10-27',
        'url': 'https://us.pycon.org/2021/'
    },
    {
        'id':3,
        'name': 'PyCon UK',
        'city': 'Birmingham',
        'country': 'UK',
        'date': '2021-09-17',
        'url': 'https://2021.pyconuk.org/'
    },
    {
        'id':4,
        'name': 'PyCon Australia',
        'city': 'Sydney',
        'country': 'Australia',
        'date': '2021-08-06',
        'url': 'https://2021.pycon-au.org/'
    },
    {
        'id':5,
        'name': 'PyCon Canada',
        'city': 'Toronto',
        'country': 'Canada',
        'date': '2021-11-12',
        'url': 'https://2021.pycon.ca/'
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