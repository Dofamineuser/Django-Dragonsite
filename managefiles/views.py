from django.shortcuts import render
from .models import File
from home.models import OwnerInfo
from blog.models import BlogCat

file = File.objects.all()
owner = OwnerInfo.objects.first()
categories = BlogCat.objects.all()


def manage_files(request):
    return render(request, 'managefiles/managefiles.html', {
        'file': file,
        'owner': owner,
        'categories': categories
    })
