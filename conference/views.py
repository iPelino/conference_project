from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_conference(request):
    list_co={
        '1':{
            'co_name':'Youth conekt',
            'co_date':'20/12/2021',
            'co_location':'Kigali Arena'
        },
        '2':{
            'co_name':'Ahazaza Conference',
            'co_date':'23/12/2021',
            'co_location':'Stade Amahoro'
        },
        '3':{
            'co_name':'Sport Updates',
            'co_date':'25/12/2021',
            'co_location':'Stade Regional'
        },
        '4':{
            'co_name':'Love Connect',
            'co_date':'28/12/2021',
            'co_location':'City Tower'
        },
        '5':{
            'co_name':'Disasters',
            'co_date':'29/12/2021',
            'co_location':'Gasabo Districtt'
        }}
    return render(request, 'lists.html',{'lists':list_co})
    
