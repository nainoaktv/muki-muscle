from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  avatar = models.ImageField(upload_true="user_avatars/", null=True, blank=True)

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_new_add=True)

class FitnessRoutine(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField()

class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  ingredients = models.TextField()
  instructions = models.TextField()

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_new_add=True)

class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_new_add=True)

class Follow(models.Model):
  follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
  following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_new_add=True)