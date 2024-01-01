from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, UserProfile, Recipe
from django.contrib.auth.models import User
from .forms import PostForm

def home(request):
    posts = Post.objects.all().order_by("-timestamp")
    return render(request, 'main/home.html', {'posts': posts})

# TODO: Add username response to profile
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     user_profile = get_object_or_404(UserProfile, user=user)
#     return render(request, 'profile/profile_detail.html', {"user_profile": user_profile, "user": user})

def profile(request, username):
    print(f"Requested username: {username}")
    user = get_object_or_404(User, username=username)
    print(f"User found: {user.username}")
    return render(request, 'profile/profile_detail.html', {"user": user})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")

    else:
        form = PostForm()
        
    return render(request, "post/create_post.html", {"form": form})

def post_detail(request, post_id):
    # return render(request, 'post/post_detail.html')
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail.html', {'post': post})
        