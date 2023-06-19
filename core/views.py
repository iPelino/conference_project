from django.shortcuts import render




def conference_list(request):
    conferences = [
        {"id":0,'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {"id":1,'name': 'Conference 2', 'dates': 'July 5-7, 2023', 'location': 'City B'},
        {"id":2,'name': 'Conference 3', 'dates': 'August 10-12, 2023', 'location': 'City C'},
        {"id":3,'name': 'Conference 4', 'dates': 'September 15-17, 2023', 'location': 'City D'},
        {"id":4,'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]
    return render(request, 'conference_list.html', {'conferences': conferences})

def conference_create(request):
    return render(request, 'conference_create.html')

def conference_details(request, conference_id):
    conferences = [
        {"id":0,'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {"id":1,'name': 'Conference 2', 'dates': 'July 5-7, 2023', 'location': 'City B'},
        {"id":2,'name': 'Conference 3', 'dates': 'August 10-12, 2023', 'location': 'City C'},
        {"id":3,'name': 'Conference 4', 'dates': 'September 15-17, 2023', 'location': 'City D'},
        {"id":4,'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]

    for item in conferences:
         if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'conference_details.html', {'conference': selectedData})

def conference_update(request, conference_id):
    conferences = [
        {"id":0,'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {"id":1,'name': 'Conference 2', 'dates': 'July 5-7, 2023', 'location': 'City B'},
        {"id":2,'name': 'Conference 3', 'dates': 'August 10-12, 2023', 'location': 'City C'},
        {"id":3,'name': 'Conference 4', 'dates': 'September 15-17, 2023', 'location': 'City D'},
        {"id":4,'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]

    for item in conferences:
         if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'conference_update.html', {'conference': selectedData})

def conference_delete(request, conference_id):
    conferences = [
        {"id":0,'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {"id":1,'name': 'Conference 2', 'dates': 'July 5-7, 2023', 'location': 'City B'},
        {"id":2,'name': 'Conference 3', 'dates': 'August 10-12, 2023', 'location': 'City C'},
        {"id":3,'name': 'Conference 4', 'dates': 'September 15-17, 2023', 'location': 'City D'},
        {"id":4,'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]

    for item in conferences:
         if (item["id"] == conference_id):
            selectedData = item
    return render(request, 'conference_delete.html', {'conference': selectedData})￼Enter
