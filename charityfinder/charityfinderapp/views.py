from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CharityForm
from .models import Charityinformation


# Create your views here.
def index_func(request):
    return render(request, 'index.html', {})


def about_func(request):
    return render(request, 'about.html', {})

def donate_func(request):
    return render(request, 'donate.html', {})

def charity_func(request):
    charity = Charityinformation.objects.all()  # select * from table ;
    return render(request, "charityform.html", {"charity": charity})
