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

def profile(request, user_id):
    # Profile view that shows a user's page with information regarding followers,
    # following, and their photos
    current_user = User.objects.get(id=user_id)
    followers = Following.objects.filter(following_id=current_user.id)
    following = Following.objects.filter(follower_id=current_user.id)
    posts = Image.objects.filter(user_id=current_user.id)

    individual_followers = []

    for follower in followers:
        individual_followers.append(follower.follower)


    return render(request, "profile.html", {"posts": posts, "following": following, "followers": followers, "individual_followers": individual_followers,"current_user": current_user})

