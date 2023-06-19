from django.contrib import admin
from .models import Speaker

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'contact_info')  # Display these fields in the list view
    search_fields = ('name', 'contact_info')  # Add search functionality for these fields
    ordering = ('name',)  # Order speakers by name
