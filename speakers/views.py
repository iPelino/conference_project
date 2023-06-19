from django.shortcuts import render
from django.shortcuts import redirect

speakers = [
    {
        "name": "John Doe",
        "bio": "John Doe is an expert in web development...",
        "other_info": "John has spoken at various conferences...",
    },
    {
        "name": "Jane Smith",
        "bio": "Jane Smith is a data scientist specializing in...",
        "other_info": "Jane has a Ph.D. in Computer Science...",
    },
    {
        "name": "Mark Johnson",
        "bio": "Mark Johnson is a renowned entrepreneur and...",
        "other_info": "Mark has been featured in several business magazines...",
    },
    {
        "name": "Sarah Johnson",
        "bio": "Sarah Johnson is a cybersecurity expert with...",
        "other_info": "Sarah has conducted extensive research on emerging cyber threats...",
    },
    {
        "name": "Michael Chen",
        "bio": "Michael Chen is a data privacy and compliance specialist...",
        "other_info": "Michael is a frequent speaker at privacy conferences...",
    },
]


def speakerList(request):
    return render(request, "speakers.html", {"speakers": speakers})


def createSpeakers(response):
    if response.method == "POST":
        speaker = {
            "name": response.POST.get("name"),
            "bio": response.POST.get("bio"),
            "other_info": response.POST.get("other_info"),
        }
        speakers.append(speaker)
        return redirect("/speakers/")
    else:
        return render(response, "createSpeaker.html")


def viewSpeaker(request, id):
    return render(request, "viewSpeaker.html", {"speaker": speakers[id - 1]})


def speakerUpdate(response, id):
    if response.method == "POST":
        speaker = {
            "name": response.POST.get("name"),
            "bio": response.POST.get("bio"),
            "other_info": response.POST.get("other_info"),
        }
        speakers[id - 1] = speaker
        return redirect("/speakers/")
    else:
        return render(response, "updateSpeaker.html", {"speaker": speakers[id - 1]})


def speakerDelete(response, id):
    if response.method == "POST":
        speakers.pop(id - 1)
        return redirect("/speakers/")
    else:
        return render(response, "deleteSpeaker.html", {"speaker": speakers[id - 1]})
