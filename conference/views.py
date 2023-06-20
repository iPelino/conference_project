# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConferenceForm
from .models import Conference

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/conference_list.html', {'conferences': conferences})


def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conference/conference_detail.html', {'conference': conference})

def create_conference(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference_list')
    else:
        form = ConferenceForm()
    return render(request, 'conference/create_conference.html', {'form': form})

def delete_conference(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        conference.delete()
        return redirect('conference_list')
    return render(request, 'conference/delete_conference.html', {'conference': conference})


def edit_conference(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            form.save()
            return redirect('conference_detail', pk=conference.pk)
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'conference/edit_conference.html', {'form': form, 'conference': conference})
