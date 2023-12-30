from django.shortcuts import render, get_object_or_404
from .models import Post, UserProfile, Recipe
from django.contrib.auth.models import User

def home(request):
    # posts = Post.object.all()
    return render(request, 'main/home.html')
    # return render(request, 'main/home.html', {'posts': posts})

# TODO: Add username response to profile
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     user_profile = get_object_or_404(UserProfile, user=user)
#     return render(request, 'profile/profile_detail.html', {"user_profile": user_profile})

def profile(request, username):
    print(f"Requested username: {username}")
    user = get_object_or_404(User, username=username)
    print(f"User found: {user.username}")
    return render(request, 'profile/profile_detail.html', {"user": user})


# TODO: Add post_id response to post_detail
def post_detail(request):
    return render(request, 'post/post_detail.html')
    # post = get_object_or_404(Post, id=post_id)
    # return render(request, 'post/post_detail.html', {'post': post})