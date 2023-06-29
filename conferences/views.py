from django.shortcuts import render

from conferences.models import Conference, Category


def conference_list(request):
    categories = Category.objects.all()[:2]
    conferences = Conference.objects.filter(category__in=categories).order_by('-start_date')
    return render(request, 'conferences/conf_list.html', {'conferences': conferences})
