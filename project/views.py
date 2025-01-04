from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello i am Home")
def about(request):
    return HttpResponse("Hello i am about")
def contact(request):
    return HttpResponse("Hello i am contact")