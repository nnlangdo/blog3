from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views.generic import ListView
from . forms import NewCommentForm,PostSearchForm
from .models import Post,Comment,Category
from django.db.models import Q
# Create your views here.



def home(request):
    posts = Post.newmanager.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog_app/index.html', context)

def post_detail(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(
        request, 
        'blog_app/post_detail.html', 
        {
        'post': post, 'comments':  user_comment, 
        'comments': comments, 
        'comment_form': comment_form
        }
    )


class CatListView(ListView):
    template_name = 'blog_app/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category']).filter(status='published')
        }
        return content

def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return context
    # to make available globaly go to settings.py and update TEMPLATES

def post_search(request):
    form = PostSearchForm()
    q = ''
    c = ''
    results = []
    query = Q()
    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            c = form.cleaned_data['c']

            if c is not None:
                query &= Q(category=c)
            if q is not None:
                query &= Q(title__contains=q)

            results = Post.objects.filter(query)
            
    return render(request, 'blog_app/search.html',
     {'form':form,
     'q':q,
     'results':results
     })