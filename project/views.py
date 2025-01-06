from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello i am Home")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("Hello i am about")
def contact(request):
    return HttpResponse("Hello i am contact")