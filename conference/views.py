from django.shortcuts import render
from django.http import HttpResponse

def conference1(request):
    conf={"1":{'cname':"Marioti conference",'date':"15/05/2023",'location':"Nyarugenge"},
        "2":{'cname':"Serena conference",'date':"16/05/2023",'location':"Gitega"},
        "3":{'cname':"Ubumwe conference",'date':"17/05/2023",'location':"Down Town"},
        "4":{'cname':"Four Points conference",'date':"18/05/2023",'location':"Kicukiro"},
        "5":{'cname':"Convertion conference",'date':"19/05/2023",'location':"Kacyiru"}}
    return render(request, 'conference1.html',{'conf':conf})
def conference(request,id):
    conf={"1":{'cname':"Marioti conference",'date':"15/05/2023",'location':"Nyarugenge"},
        "2":{'cname':"Serena conference",'date':"16/05/2023",'location':"Gitega"},
        "3":{'cname':"Ubumwe conference",'date':"17/05/2023",'location':"Down Town"},
        "4":{'cname':"Four Points conference",'date':"18/05/2023",'location':"Kicukiro"},
        "5":{'cname':"Convertion conference",'date':"19/05/2023",'location':"Kacyiru"}}
    id1=id
    return render(request, 'conference.html',{'id1':id1,'conf':conf})

def update(request,id):
    conf={"1":{'cname':"Marioti conference",'date':"15/05/2023",'location':"Nyarugenge"},
        "2":{'cname':"Serena conference",'date':"16/05/2023",'location':"Gitega"},
        "3":{'cname':"Ubumwe conference",'date':"17/05/2023",'location':"Down Town"},
        "4":{'cname':"Four Points conference",'date':"18/05/2023",'location':"Kicukiro"},
        "5":{'cname':"Convertion conference",'date':"19/05/2023",'location':"Kacyiru"}}
    id1=id
    return render(request, 'update.html',{'id1':id1,'conf':conf})

def deleteConf(request,id):
    conf={"1":{'cname':"Marioti conference",'date':"15/05/2023",'location':"Nyarugenge"},
        "2":{'cname':"Serena conference",'date':"16/05/2023",'location':"Gitega"},
        "3":{'cname':"Ubumwe conference",'date':"17/05/2023",'location':"Down Town"},
        "4":{'cname':"Four Points conference",'date':"18/05/2023",'location':"Kicukiro"},
        "5":{'cname':"Convertion conference",'date':"19/05/2023",'location':"Kacyiru"}}
    id1=id
    return render(request, 'deleteConf.html',{'id1':id1,'conf':conf})

def CreateConf(request):
    return render(request, 'addconf.html')

# Create your views here.
