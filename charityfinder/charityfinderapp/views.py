from django.shortcuts import render
from.forms import CharityForm

# Create your views here.
def charity(request):
    form = CharityForm()
    return render(request,'charityform.html',{'form':form})