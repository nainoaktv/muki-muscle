from django.shortcuts import render, get_object_or_404
from .models import Post, UserProfile, Recipe

def home(request):
    # posts = Post.object.all()
    return render(request, 'main/home.html')
    # return render(request, 'main/home.html', {'posts': posts})

# def profile(request, username):
#     user_profile = get_object_or_404(UserProfile, username=username)
#     return render(request, 'main/profile.html', {'user_profile': user_profile})

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, 'main/post_detail.html', {'post': post})

