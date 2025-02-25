from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import posts
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import postSerializer
from rest_framework import status

class post_view(APIView):
    def get(self, request, pk = None):
        if pk:  # If a primary key is provided
            try:
                post_instance = posts.objects.get(pk=pk)  # Fetch a specific post
            except posts.DoesNotExist:
                return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = postSerializer(post_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Otherwise, fetch all posts
        post_queryset = posts.objects.all()
        serializer = postSerializer(post_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # POST request ke liye
    def post(self, request):
        serializer = postSerializer(data=request.data)  # Incoming data serialize karein
        if serializer.is_valid():  # Validation check karein
            serializer.save()  # Valid data save karein
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # PUT: Update an existing post
    def put(self, request, pk):
        try:
            post_instance = posts.objects.get(pk=pk)  # Retrieve the specific post
        except posts.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = postSerializer(post_instance, data=request.data)  # Bind incoming data to existing instance
        if serializer.is_valid():
            serializer.save()  # Save the updated data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                user = User(
                    username = userName,
                    first_name = firstName,
                    last_name = lastName
                    )
                user.set_password(password1)
                user.save() 
            return HttpResponse("User succesfully created")
    return render(req, 'register.html' )

def userLogin(req):
    if req.method == 'POST':
        userName = req.POST.get('userName')
        password1 = req.POST.get('password1')
        user = authenticate(username=userName, password = password1 )
        if user is not None:
            login(req, user)
            return redirect('home')
    return render(req, 'login.html')

def userLogout(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')
    return render(req, 'logout.html')


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
