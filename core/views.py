from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from conference.models import Conference

class ConferenceListView(ListView):
    model = Conference
    template_name = 'conference/conference_list.html'

class ConferenceCreateView(CreateView):
    model = Conference
    template_name = 'conference/conference_form.html'
    fields = ['name', 'dates', 'location', 'topics']
    success_url = reverse_lazy('conference_list')

class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conference/conference_detail.html'

class ConferenceUpdateView(UpdateView):
    model = Conference
    template_name = 'conference/conference_form.html'
    fields = ['name', 'dates', 'location', 'topics']
    success_url = reverse_lazy('conference_list')

class ConferenceDeleteView(DeleteView):
    model = Conference
    template_name = 'conference/conference_delete.html'
    success_url = reverse_lazy('conference_list')
