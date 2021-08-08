from django import forms

from .models import Comment

# Create class for add meta to field for form --> from database (models)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')