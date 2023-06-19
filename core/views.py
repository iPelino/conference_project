from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'testing.html', {'number': number})
    def speaker(request):
    #return HttpResponse("speaker of the day is you man")
    context ={'speakers':speakers}
    return render(request,'speakers.html',context)
def createspeaker(request):
 #return HttpResponse("create speaker man")
 return render(request,'create.html')
def individualspeaker(request,pk):
   speaker = None
   for i in speakers:
      if i['id']== int(pk):
         speaker = i
         contexts = {'speaker':speaker}
   return render(request,'individualspeaker.html',contexts)

def updatespeaker(request,pk):
   speaker = None
   for i in speakers:
    if i['id'] == int(pk):
       speaker = i
       context = {'speaker':speaker}
   return render(request,'updatespeaker.html',context)

def deletespeaker(request,pk):
   speaker = None
   for i in speakers:
    if i['id'] == int(pk):
       speaker = i
       context = {'speaker':speaker}
       return render(request,'deletespeaker.html',context)
    
