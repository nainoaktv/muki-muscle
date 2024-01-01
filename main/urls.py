from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('post/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]