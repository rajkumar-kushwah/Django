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

def update(req, id):
    post = posts.objects.all()
    updatePost = get_object_or_404(posts, id = id)
    if req.method == 'POST':
<<<<<<< Updated upstream
=======
        post.image = req.FILES.get('image')
        post.title = req.POST.get('title')
        post.des = req.POST.get('des')
        post.save()
        return HttpResponse("data edit successfully")
    return render(req, 'app.html', {"ram": post, "posts": postss})


def update(req,id):
    post = posts.objects.all()
    updatePost = get_object_or_404(posts,id = id)
    if req.method == 'POST':
>>>>>>> Stashed changes
        updatePost.image = req.FILES.get('image')
        updatePost.title = req.POST.get('title')
        updatePost.des = req.POST.get('des')
        updatePost.save()
        return HttpResponse("update post")
<<<<<<< Updated upstream
    return render(req, 'app.html' , {"posts": post, "update": updatePost})

def DeletePost(req, id):
    post = get_object_or_404(posts , id=id)
    post.delete()
    return HttpResponse("the post id deleted")
=======
    return render(req, 'app.html' ,{"posts": post, "update":updatePost})

def delete(req , id):
    
    post=get_object_or_404(posts,id=id)
    post.delete()
    return HttpResponse(" the post deleted")
>>>>>>> Stashed changes
