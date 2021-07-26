from django import forms
from django.db import models
from django.db.models import fields

from .models import Comment

class CommentForm(forms.ModelForm):
    # Create meta class for add field for form - from database (models)
    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')