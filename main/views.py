from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, UserProfile, Recipe
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from .forms import PostForm, SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

# ! current_user needs to be called for each view that needs to use "Profile" navlink
# ? Just get rid of profile navlink to avoid repetitive code
# TODO: Find out if there is a better way to use Profile nav link to route to current user


# * Auth Views
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

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("user_login")

# * Routes
def home(request):
    current_user = request.user
    if not request.user.is_authenticated:
        return redirect("user_login")

    posts = Post.objects.all().order_by("-timestamp")

    for post in posts:
        time_since = timesince(post.timestamp)

        if 'hour' in time_since:
            hours_since = time_since.split(',')[0]
            post.display_time = f'{hours_since}'
        else:
            post.display_time = f'{time_since}'
            
    return render(request, 'main/home.html', {'posts': posts, "current_user": current_user, })

def profile(request, username):
    current_user = request.user
    print(f"This is the current user: {current_user}")
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)

    if not username:
        return HttpResponseBadRequest("Invalid Username")
        
    
    if user:
        return render(request, 'profile/show.html', {
            "current_user": current_user,
            "user": user, 
            "posts": posts,
        })

# * Posts
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


# TODO: Details need to include > comments, likes, reposts, username for each comment.
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail.html', {'post': post})

