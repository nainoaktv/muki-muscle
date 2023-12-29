from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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

class Hashtag(models.Model):
  name = models.CharField(max_length=50, unique=True)

class PostHashtag(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

class FitnessChallenge(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  start_date = models.TextField()
  end_date = models.TextField()

class Chat(models.Model):
  participants = models.ManyToManyField(User, related_name="chats")

class Message(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  sender = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_new_add=True)

class Activity(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey("content_type", "object_id")
  timestamp = models.DateTimeField(auto_new_add=True)