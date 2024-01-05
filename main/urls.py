from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('user_profile/<int:user_id>/', views.show_profile, name='show_profile'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]