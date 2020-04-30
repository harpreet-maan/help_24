from django.shortcuts import render
from webapp.models import videos,employees
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
def home(request):
    video=videos.objects.all()
    return render(request,'home.html',{'video':video})

def details(request,pk):
    v=videos.objects.get(pk=pk)
    return render(request,'details.html',{'v':v})
