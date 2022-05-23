from django.shortcuts import render
from .models import Blog, BlogCat


def blog(request):
    blog = Blog.objects.all()
    categories = BlogCat.objects.all()
    return render(request, 'blog/blog.html', {
        'blog': blog,
        'categories': categories
    })
