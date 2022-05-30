from django.shortcuts import render
from .models import *
from blog.models import Blog
from blog.views import ukr_month

# Create your views here.


def index(request):
    team = Team.objects.all()
    blog = list(Blog.objects.reverse()[1:])
    owner = OwnerInfo.objects.first()
    print(blog)
    return render(request, 'home/index.html', {
        "team": team,
        "blog": blog,
        "owner": owner,
        'ukr_month': ukr_month
    })
