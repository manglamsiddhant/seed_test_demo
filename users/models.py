from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar and hasattr(self.avatar, 'path'):
            try:
                img = Image.open(self.avatar.path)

                if img.height > 100 or img.width > 100:
                    new_img = (100, 100)
                    img.thumbnail(new_img)
                    img.save(self.avatar.path)
            except FileNotFoundError:
                pass  # Default image might not physically exist yet



class DuelMatch(models.Model):
    initiator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="initiated_matches")
    opponent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="opponent_matches")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_matches")

    def __str__(self):
        return f"{self.initiator.username} vs {self.opponent.username}"
    

class ChatSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10, choices=[('user', 'User'), ('ai', 'AI')])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateField()

class DailyNewsRead(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    read_date = models.DateField(auto_now_add=True)

class Streak(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    current_length = models.IntegerField(default=1)

# users/models.py

class CustomUser(AbstractUser):
    # Add a new optional field
    location = models.CharField(max_length=100, blank=True, null=True)



