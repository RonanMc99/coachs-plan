from django.shortcuts import render
from django.views import generic

from .models import Post


def post_list(request):
    # display a list of published posts ordered by publish date
    queryset = Post.objects.filter(
        status="published",
    ).order_by("publish")
    context = {"queryset": queryset}
    return render(request, "blog-list.html", context)
