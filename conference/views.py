# views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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