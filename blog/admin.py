from django.contrib import admin
from django.db import models
from django.db.models.base import Model

from .models import Comment, Post

admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'post']