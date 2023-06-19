from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Speaker

class SpeakerListView(ListView):
    model = Speaker
    paginate_by = 10
    template_name = 'speakers/speaker_list.html'
    context_object_name = 'speakers'

class SpeakerCreateView(CreateView):
    model = Speaker
    fields = ['name', 'bio', 'contact_info']
    template_name = 'speakers/speaker_form.html'
    success_url = reverse_lazy('speakers:speaker_list')

class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = 'speakers/speaker_detail.html'
    context_object_name = 'speaker'

class SpeakerUpdateView(UpdateView):
    model = Speaker
    fields = ['name', 'bio', 'contact_info']
    template_name = 'speakers/speaker_form.html'

    def get_success_url(self):
        return reverse_lazy('speakers:speaker_detail', kwargs={'speaker_id': self.object.id})

class SpeakerDeleteView(DeleteView):
    model = Speaker
    template_name = 'speakers/speaker_confirm_delete.html'
    success_url = reverse_lazy('speakers:speaker_list')
