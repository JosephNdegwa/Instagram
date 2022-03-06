from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import *
from .models import Image, Profile, Following

def homepage(request):
    # Homepage view displaying the user's timeline and suggestions for people they can 
    # choose to follow
    following = Following.objects.filter(follower_id=request.user.id)

    images = []
    for follow in following:
        images.append(Image.objects.filter(user_id=follow.following.id)) 

    if request.user.is_authenticated:
        users = User.objects.all()[:3]
        return render(request, 'index.html', {"users": users, "images": images}) 
    else:
        return render(request, 'index.html') 

