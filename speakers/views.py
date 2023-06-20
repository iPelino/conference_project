from django.http import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
speakers = [
   { 'id':1,'name':"samuel","bio":"software developer",'email':"eric@mail.com" },
    {'id':2,'name':"eric","bio":"software developer",'email':"eric@mail.com"},
     {
      'id':3,'name':"david","bio":"software developer",'email':"cedricc@mail.com"
   },
    {
      'id':4,'name':" messi","bio":"network developer",'email':"eric@mail.com"
   },
    {
      'id':5,'name':"samuel","bio":"software developer",'email':"samuelic@mail.com"
   },
]

def home(request):
    #return HttpResponse("HOME page")
    return render(request,'home.html')
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
   return render(request,'singlespeaker.html',contexts)

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