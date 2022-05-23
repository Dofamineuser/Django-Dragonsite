from django.shortcuts import render
from .models import *
from blog.models import Blog

# Create your views here.


def index(request):
    team = Team.objects.all()
    blog = Blog.objects.all()
    owner = OwnerInfo.objects.first()
    return render(request, 'home/index.html', {
        "team": team,
        "blog": blog,
        "owner": owner
    })
