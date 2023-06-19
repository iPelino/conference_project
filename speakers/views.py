from django.shortcuts import render

# Create your views here.
def view_speakers (request):
    speakers = {'johovanis' : 24,
                'Benine': 24,
                'kendra': 30,
                'Doreen': 22,
                'Angel': 29,
                }
    return render(request,'speaker.html', {'speakers' : speakers})
