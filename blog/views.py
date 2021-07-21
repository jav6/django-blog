from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-post_title')[:5]
    context = {'latest_post_list':latest_post_list}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post':post}
    return render(request, 'blog/detail.html', context)