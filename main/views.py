from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, UserProfile, Recipe
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from .forms import PostForm, SignupForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {'form': form})


def home(request):
    posts = Post.objects.all().order_by("-timestamp")

    for post in posts:
        time_since = timesince(post.timestamp)

        if 'hour' in time_since:
            hours_since = time_since.split(',')[0]
            post.display_time = f'{hours_since}'
        else:
            post.display_time = f'{time_since}'
            
    return render(request, 'main/home.html', {'posts': posts})

# * Show logged in users profile
def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(user=user)
    print(f"User posts: {user_posts} made by {user}")
    return render(request, 'profile/profile_detail.html', {"user": user, "user_posts": user_posts})

# * Show another user profile
def show_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(f"Currently viewing {user.username}")
    posts = Post.objects.filter(user=user)
    return render(request, 'profile/show.html', {"user": user, "posts": posts})

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
        