from django.shortcuts import render

# Create your views here.
conferences = [
        {
            "id": 1,
            "name": "SCA contributhon",
            "date": "2023-03-12",
            "location": "Raddison Blu"
        },
        {
            "id": 2,
            "name": "Women in stem",
            "date": "2023-12-12",
            "location": "Kigali conventionn center"
        },
        {
            "id": 3,
            "name": "Code beta solutions",
            "date": "2023-04-02",
            "location": "Kigali Heights"
        },

        {
            "id": 4,
            "name": "Africa science week",
            "date": "2024-01-01",
            "location": "Park inn"
        },

        {
            "id": 5,
            "name": "Kigali founders happy hour",
            "date": "2024-07-01",
            "location": "Ubumwe Hotel"
        },
    ]
def conferences_view(request):
    return render(request, 'confs.html', context={"conferences": conferences})
def create_conference_view(request):
    return render(request, 'create_confs.html')

def conference_id(request):
    return render(request, 'confs_id.html')

def conference_update(request):
    return render(request, 'confs_update.html')