from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CharityForm
from charityfinderapp.models import Charityinformation


# Create your views here.

def charity(request):
    charity = Charityinformation.objects.all()  # select * from table ;
    return render(request, "charityform.html", {"charity": charity})
