from django.http import HttpResponse
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














# def about_view(request):
#     return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


# def testing_stuff(request, number):
#     # DB query
#     #
#     # number = ''
#     # if id < 5:
#     #     number = 'xzy'
#     return render(request, 'testing.html', {'number': number})