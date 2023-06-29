from django.contrib import admin
from conferences.models import Conference, Category


# Register your models here.


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'start_date',
        'end_date', 'venue', 'entry_fee',
    ]
    list_filter = ['start_date', 'end_date', 'entry_fee']
    search_fields = ['title', 'category__name']


# admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Category)
