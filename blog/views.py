from django.shortcuts import render
from django.views import generic

from .models import Post

def post_list(request):
    # display a list of published posts
    queryset = Post.objects.filter(status='published')
    context = {
        'queryset': queryset
    }
    return render(request, "blog-list.html", context)
