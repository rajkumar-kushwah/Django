from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import posts
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def createUser(req):
    if req.method == 'POST':
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        userName = req.POST.get('userName')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=userName).exists():
                messages.info(req, "user already exists")
                return redirect("/register/")
            else:
                user = User(password = password1, username = userName)
                user.first_name = firstName
                user.last_name = lastName
                user.save() 
            return HttpResponse("User succesfully created")
    return render(req, 'register.html' )

def userLogin(req):
    if req.method == 'POST':
        userName = req.POST.get('userName')
        password1 = req.POST.get('password1')
        user = authenticate(req, username = userName, password = password1)
        if user is not None:
            login(req, user)
            return redirect(home)
    return render(req, 'login.html')



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
        updatePost.image = req.FILES.get('image')
        updatePost.title = req.POST.get('title')
        updatePost.des = req.POST.get('des')
        updatePost.save()
        return HttpResponse("update post")
    return render(req, 'app.html' , {"posts": post, "update": updatePost})

def DeletePost(req, id):
    post = get_object_or_404(posts , id=id)
    post.delete()
    return HttpResponse("the post id deleted")