from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Speaker

# List of all speakers
class SpeakerListView(ListView):
    model = Speaker
    paginate_by = 8
    template_name = 'speakers/speaker_list.html'
    context_object_name = 'speakers'

# Form to create a new speaker
class SpeakerCreateView(CreateView):
    model = Speaker
    fields = ['name', 'bio', 'email','contact_information']
    template_name = 'speakers/speaker_form.html'
    success_url = reverse_lazy('speakers:speaker_list')

# Details of a specific speaker
class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = 'speakers/speaker_detail.html'
    context_object_name = 'speaker'

# Form to update a specific speaker
class SpeakerUpdateView(UpdateView):
    model = Speaker
    fields = ['name', 'bio', 'email', 'contact_information']
    template_name = 'speakers/speaker_form.html'
    context_object_name = 'speaker'
    success_url = reverse_lazy('speakers:speaker_list')

# Form to delete a specific speaker
class SpeakerDeleteView(DeleteView):
    model = Speaker
    template_name = 'speakers/speaker_confirm_delete.html'
    context_object_name = 'speaker'
    success_url = reverse_lazy('speakers:speaker_list')