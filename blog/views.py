from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 6

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context ={
        'post':post,
        'new_comment': new_comment,
        'comment_form': comment_form,
        }
    return render(request, 'blog/detail.html', context)