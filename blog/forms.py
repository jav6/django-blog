from django import forms
from django.db import models
from django.db.models import fields

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')