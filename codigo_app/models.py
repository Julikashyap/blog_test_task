from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class SignupForm(AbstractUser):
    name = models.CharField(max_length=50,blank=True,null=True)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(SignupForm, on_delete=models.CASCADE, related_name='blog_user')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(SignupForm, on_delete=models.CASCADE, related_name='comment_user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog')