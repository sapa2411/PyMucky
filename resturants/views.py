import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function based views
def home(request):
    num = random.randint(0, 100000)
    return render(request, 'home.html', {"html_var": "Context Variable", "rand_num": num})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})
