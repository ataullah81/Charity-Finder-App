from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import CharityForm
from .forms import ContactForm
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


def search_charity_func(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        charityname = Charityinformation.objects.filter(charity_name__contains=searched)
        return render(request, 'search_charity.html', {'searched': searched, 'charityname': charityname})
    else:
        return render(request, 'search_charity.html', {})

def contact_func(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})