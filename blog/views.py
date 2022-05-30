from django.shortcuts import render
from .models import Blog, BlogCat
from home.models import OwnerInfo
from django.template.defaulttags import register


@register.filter
def get_key(dict, key):
    return dict.get(str(key))


ukr_month = {
    "1": "Січень",
    "2": "Лютий",
    "3": "Березень",
    "4": "Квітень",
    "5": "Травень",
    "6": "Червень",
    "7": "Липень",
    "8": "Серпень",
    "9": "Вересень",
    "10": "Жовтень",
    "11": "Листопад",
    "12": "Грудень"
}


def blog(request):
    blog = Blog.objects.all()
    categories = BlogCat.objects.all()
    owner = OwnerInfo.objects.first()
    return render(request, 'blog/blog.html', {
        'blog': blog,
        'categories': categories,
        'owner': owner,
        'ukr_month': ukr_month
    })
