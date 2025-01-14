from django.shortcuts import render, redirect, get_object_or_404
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

def edit(req, id):
    postss = posts.objects.all()
    print(id)
    post = get_object_or_404(posts, id=id)
    if req.method == 'POST':
        post.image = req.FILES.get('image')
        post.title = req.POST.get('title')
        post.des = req.POST.get('des')
        post.save()
        return HttpResponse("data edit successfully")
    return render(req, 'app.html', {"ram": post, "posts": postss})