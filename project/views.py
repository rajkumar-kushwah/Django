from django.http import HttpResponse
from django.shortcuts import rendere

def Home(request):
    # return HttpResponse("Hello i am Home")
    return rendere(request, 'index.html')
def about(request):
    return HttpResponse("Hello i am about")
def contact(request):
    return HttpResponse("Hello i am contact")