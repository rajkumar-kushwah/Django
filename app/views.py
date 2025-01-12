from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts

# Create your views here.

def home(req):
    if req.method == 'POST':
        image = req.POST.get('image')
        title = req.POST.get('title')
        des = req.POST.get('des')

        post = posts(title = title, des= des, image = image)
        post.save()
        return HttpResponse("data added successfully")
    return render(req, 'app.html', )
