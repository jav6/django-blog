from django.shortcuts import render, get_object_or_404

from .models import Post, Comment

def index(request):
    latest_post_list = Post.objects.order_by('-post_title')[:5]
    context = {'latest_post_list':latest_post_list}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        comment = Comment.objects.get(pk=post_id)
    except:
        comment = False
    context = {'post':post, 'comment':comment}
    return render(request, 'blog/detail.html', context)