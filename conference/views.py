from django.shortcuts import render
from django.http import HttpResponse

def listconference(request):
    conferences={'1':{'name':'Social Affairs','date':'1/1/2025','location':'Lectures room'},
                '2':{'name':'Education','date':'2/1/2025','location':'Muhabura'},
                '3':{'name':'E-Health','date':'3/1/2025','location':'Kiyovu'},
                '4':{'name':'Public Talk','date':'4/1/2025','location':'Nyarugenge'},
                '5':{'name':'Entertainment','date':'5/1/2025','location':'Arena'}
                }
    return render(request, 'view_conference.html',{'conference':conferences})

