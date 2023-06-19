from django.shortcuts import render, get_object_or_404
from conference.models import Conference

def conference_list(request):
    # Retrieve a list of conferences
    conferences = Conference.objects.all()[:5]  # Assuming you have a Conference model
    
    # Pass the conference list to the template for rendering
    return render(request, 'conference/conference_list.html', {'conferences': conferences})

def conference_create(request):
    # Render the form to create a new conference (static form)
    return render(request, 'conference/conference_create.html')

def conference_details(request, conference_id):
    # Retrieve the conference based on its ID
    conference = get_object_or_404(Conference, pk=conference_id) # Render the form to update the conference (filled with static dummy information)
    return render(request, 'conference/conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    # Retrieve the conference based on its ID
    conference = get_object_or_404(Conference, pk=conference_id)
    
    # Render the confirmation form to delete the conference
    return render(request, 'conference/conference_delete.html', {'conference': conference})
