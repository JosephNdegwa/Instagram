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


def profile_follow(request):
    followed_user = User.objects.get(id=request.POST['id'])

    # if already being followed
    if Following.objects.filter(follower_id=request.user, following_id=followed_user.id):
        # get the information for the user's profile
        followers = Following.objects.filter(following_id=followed_user.id)
        following = Following.objects.filter(follower_id=followed_user.id)
        posts = Image.objects.filter(user_id=followed_user.id)

        individual_followers = []

        for follower in followers:
            individual_followers.append(follower.follower)
        
        return redirect("profile", user_id=followed_user.id)
    else:
        follow = Following(follower=request.user, following=followed_user) 
        follow.save()

        # get the information for the user's profile
        followers = Following.objects.filter(following_id=followed_user.id)
        following = Following.objects.filter(follower_id=followed_user.id)
        posts = Image.objects.filter(user_id=followed_user.id)

        return redirect("profile", user_id=followed_user.id)


def profile_unfollow(request):
    unfollowed_user = User.objects.get(id=request.POST['id'])
    follow = Following.objects.filter(follower_id=request.user.id, following_id=unfollowed_user.id)
    follow.delete()

    followers = Following.objects.filter(following_id=unfollowed_user.id)
    following = Following.objects.filter(follower_id=unfollowed_user.id)
    posts = Image.objects.filter(user_id=unfollowed_user.id)

    individual_followers = []

    for follower in followers:
        individual_followers.append(follower.follower)

    
    return redirect("profile", user_id=unfollowed_user.id)

