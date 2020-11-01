from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post
from plans.models import Coach


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
    coach = Coach.objects.get(slug=post.author.slug)
    context = {
        "post": post,
        "coach": coach,
    }
    return render(request, "blog-detail.html", context)

def coach_view(request, slug):
    # display a list of published posts filtered by coach
    coach = Coach.objects.get(slug=slug)
    queryset = Post.objects.filter(author=coach)
    context = {
        "queryset": queryset,
        "coach": coach
    }
    return render(request, "coach-posts.html", context)
