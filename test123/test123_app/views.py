from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def page_2(request):
    return render(request, 'page_2.html')
