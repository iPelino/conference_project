from django.shortcuts import render

# Conference list view
def conference_list(request):
    conferences = [
        {'name': 'Conference 1', 'dates': 'June 1-3, 2022', 'location': 'City A'},
        {'name': 'Conference 2', 'dates': 'July 15-17, 2022', 'location': 'City B'},
        {'name': 'Conference 3', 'dates': 'August 5-7, 2002', 'location': 'City C'},
        {'name': 'Conference 4', 'dates': 'September 10-12, 2006', 'location': 'City D'},
        {'name': 'Conference 5', 'dates': 'October 20-22, 2023', 'location': 'City E'},
    ]
    return render(request, 'conference_app/conference_list.html', {'conferences': conferences})

# Create conference view

def create_conference(request):
    return render(request, 'conference_app/create_conference.html')

# Conference details view
def conference_details(request, conference_id):
    conference = {
        'name': 'Conference 1',
        'dates': 'June 1-3, 2023',
        'location': 'City A',
        'topics': 'Topic 1, Topic 2, Topic 3',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    }
    return render(request, 'conference_app/conference_details.html', {'conference': conference})
