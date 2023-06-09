from django.shortcuts import render
from django.http import HttpResponse
from home.models import About
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        abt = About(name = name, email = email, phone = phone, date= datetime.today())
        abt.save()
        messages.success(request, "Your Information is saved")
    
    return render(request, 'about.html')
#https://source.unsplash.com/random/1280x720/?cars