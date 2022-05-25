from django.shortcuts import render
from .models import Blog, BlogCat
from home.models import OwnerInfo


def blog(request):
    blog = Blog.objects.all()
    categories = BlogCat.objects.all()
    owner = OwnerInfo.objects.first()
    return render(request, 'blog/blog.html', {
        'blog': blog,
        'categories': categories,
        'owner': owner
    })
