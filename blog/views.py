from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


def post_list(request):
    # display a list of published posts ordered by publish date
    queryset = Post.objects.filter(
        status="published",
    ).order_by("publish")
    context = {"queryset": queryset}
    return render(request, "blog-list.html", context)

def post_detail(request, slug):
    # display a list of the chapters in this book
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, "blog-detail.html", context)
