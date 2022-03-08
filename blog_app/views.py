from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Post
# Create your views here.



def home(request):
    posts = Post.newmanager.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog_app/index.html', context)

def post_detail(request,post):
    post = get_object_or_404(Post, slug=post, status='published')
    context = {
        'post':post
    }
    return render(request, 'blog_app/post_detail.html', context)