from django.shortcuts import render
from . import conference_data


def all_conferences(request):
    return render(request, 'conference/home.html', {'conference_list': conference_data.conference_list})


def create_conference(request):
    if request.method == 'POST':
        conference = {
            'id': int(request.POST.get('id')),
            'title': request.POST.get('title'),
            'date_time': request.POST.get('date'),
            'location': request.POST.get('location'),
            'hosting_organization': request.POST.get('organization'),
            'topics': request.POST.get('topics'),
        }
        conference_data.conference_list.append(conference)
        return render(request, 'conference/home.html', {'message': 'new conference created!'})
    return render(request, 'conference/create-conference-form.html')


def view_single_conference(request, id):
    conference = None
    for single_conference in conference_data.conference_list:
        if single_conference["id"] == id:
            conference = single_conference
            break
    if conference:
        data = {'conference': conference}
    else:
        data = {'conference': None}
    return render(request, 'conference/single_conference.html', data)


def update_conference(request, id):
    conference_to_update = None
    for conference in conference_data.conference_list:
        if conference['id'] == id:
            conference_to_update = conference
            break
    if request.method == "GET":
        return render(request, 'conference/update-conference-form.html', {'conference': conference_to_update})
    elif request.method == 'POST':
        conference_to_update['id']['title'] = request.POST.get('title')
        conference_to_update['id']['date_time'] = request.POST.get('date')
        conference_to_update['id']['location'] = request.POST.get('location')
        conference_to_update['id']['hosting_organization'] = request.POST.get(
            'organization')
        topics_input = request.POST.get('topics')
        conference_to_update['id']['topics'] = [topic.strip()
                                                for topic in topics_input.split(',') if topic.strip()]
        messages.success(request, 'Conference updated successfully.')
        return redirect('conference_list')
    messages.error(request, 'Failed to update conference.')
    return redirect('conference_list')


def delete_conference(request, id):
    single_conference = None
    for conference in conference_data.conference_list:
        if conference['id'] == id:
            single_conference = conference
            break
    if request.method == "POST":
        conference_data.conference_list.remove(single_conference)
        return redirect('conference_list')

    return render(request, 'conference/confirmation-page.html', {'conference': single_conference})
