from django.shortcuts import render, get_object_or_404
from .models import Conference

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})

def conference_create(request):
    return render(request, 'conference_create.html')

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference_detail.html', {'conference': conference})

def conference_update(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference_update.html', {'conference': conference})

def conference_delete(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference_delete.html', {'conference': conference})
