from django.shortcuts import render

def conference_list(request):
    conferences = [
        {'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {'name': 'Conference 2', 'dates': 'July 5-7, 2023', 'location': 'City B'},
        {'name': 'Conference 3', 'dates': 'August 10-12, 2023', 'location': 'City C'},
        {'name': 'Conference 4', 'dates': 'September 15-17, 2023', 'location': 'City D'},
        {'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]
    return render(request, 'conference/conference_list.html', {'conferences': conferences})

def conference_create(request):
    return render(request, 'conference/conference_create.html')

def conference_details(request, conference_id):
    conference = {'name': 'Conference', 'dates': 'June 1-3, 2023', 'location': 'City A', 'topics': 'Topic 1, Topic 2'}
    return render(request, 'conference/conference_details.html', {'conference': conference})

def conference_update(request, conference_id):
    conference = {'name': 'Conference', 'dates': 'June 1-3, 2023', 'location': 'City A', 'topics': 'Topic 1, Topic 2'}
    return render(request, 'conference/conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    conference = {'name': 'Conference', 'dates': 'June 1-3, 2023', 'location': 'City A', 'topics': 'Topic 1, Topic 2'}
    return render(request, 'conference/conference_delete.html', {'conference': conference})
