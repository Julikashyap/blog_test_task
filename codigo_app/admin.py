from django.contrib import admin
from .models import *

# Register your models here.

class SignupFormAdmin(admin.ModelAdmin):
    list_display=('id','name', 'email', 'username', 'first_name', 'last_name')

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title', 'content', 'created_at', 'updated_at', 'user')

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','comment', 'created_at', 'updated_at', 'user', 'blog')

class TagAdmin(admin.ModelAdmin):
    list_display=('id','name')

admin.site.register(SignupForm, SignupFormAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)