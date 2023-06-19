from django.shortcuts import render

# Create your views here.
def list_conferences(request):
    return render(request,'conferences.html')

def create_new(request):
    return render(request,'create.html')
