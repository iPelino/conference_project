from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Conferences

def conference(request):
    data = Conferences.objects.all().values()
    template = loader.get_template('conference.html')
    conferences_data = {
        'conference': data
    }
    return HttpResponse (template.render(conferences_data, request ))

def create_conference(request):

    return render(request, 'createconference.html', )

def view_conference(request, conference_id):
    data = Conferences.objects.all().values()
    conferences_data = {
        'conference': data
    }
    return render(request, 'singleconference.html',conferences_data)

def update_conference(request, conference_id):
    data = Conferences.objects.all().values()
    conferences_data = {
        'conference': data
    }
    return render(request, 'updateConference.html',conferences_data)

def delete_conference(request, conference_id):
    data = Conferences.objects.all().values()
    delete_item = [item for item in data if item['id'] ==conference_id ]
    conferences_data = {
        'conference': delete_item
    }
    return render(request, 'deleteconference.html', conferences_data)

# Create your views here.
