from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts

# Create your views here.

def home(req):
    post = posts.objects.all()
    if req.method == 'POST':
        image = req.FILES.get('image')
        title = req.POST.get('title')
        des = req.POST.get('des')

        post = posts(title = title, des= des, image = image)
        post.save()
        return HttpResponse("data added successfully")
    return render(req, 'app.html', {"posts": post})
