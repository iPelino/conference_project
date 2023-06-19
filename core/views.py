from django.shortcuts import render

conferences = [
    {
        "id": 1,
        "name": "Conferencia de Ciencias de la Salud",
        "location": "Main hall 1",
        "start": "2020-07-02",
        "end": "2020-07-09"
    },
    {
        "id": 2,
        "name": "Tech Summit 2021",
        "location": "Conference Center",
        "start": "2021-09-15",
        "end": "2021-09-17"
    },
    {
        "id": 3,
        "name": "Marketing Conference",
        "location": "Grand Hotel",
        "start": "2022-05-20",
        "end": "2022-05-22"
    },
    {
        "id": 4,
        "name": "Design Symposium",
        "location": "Art Gallery",
        "start": "2023-03-10",
        "end": "2023-03-12"
    },
    {
        "id": 5,
        "name": "Startup Expo",
        "location": "Innovation Hub",
        "start": "2023-08-05",
        "end": "2023-08-07"
    }
]


def render_conference_list(request):
    """
    Render a list of conferences
    """
    return render(request, 'home.html', {"conferences": conferences});

def create_conference(request):
    """
    Create a new Conferencing 
    """
    return render(request, 'create_conference.html')

def render_conference(request, conference_id: int):
    """
    render a specific conference
    """
    for conference in conferences:
        if conference.get('id') == conference_id:
            return render(request,'conference.html', {"conference": conference})
    return render(request, 'error.html', {"error": "Conference not found"}) 
    

def update_conference(request, conference_id: int):
    """
    update a specific conference's details
    """
    for conference in conferences:
        if conference.get('id') == conference_id:
            return render(request, 'update_conference.html', {"conference": conference})
    return render(request, 'error.html', {"error": "Conference not found"}) 

def delete_conference(request, conference_id: int):
    """
    remove a conference from the conferences list
    """
    for conference in conferences:
        if conference.get('id') == conference_id:
            return render(request, 'delete_conference.html', {"conference": conference})
    return render(request, 'error.html', {"error": "Conference not found"}) 









# def about_view(request):
#     return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


# def testing_stuff(request, number):
#     # DB query
#     #
#     # number = ''
#     # if id < 5:
#     #     number = 'xzy'
#     return render(request, 'testing.html', {'number': number})