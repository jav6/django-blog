from django.contrib import admin
from django.db import models
from django.db.models.base import Model

from .models import Comment, Image, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('post_title', 'post_slug', 'post_img', 'post_body')
    list_display = ('post_title', 'post_slug', 'post_img')
    prepopulated_fields = {'post_slug': ('post_title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'post']

admin.site.register(Image)