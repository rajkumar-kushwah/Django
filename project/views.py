from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello i am Home")