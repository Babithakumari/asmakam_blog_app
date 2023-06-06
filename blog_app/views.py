from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.


def index(request):
    return render(request, "blog_app/layout.html")

def blog_post_all(request):

    return render(request, "blog_app/blog_post_all.html",{
        "blog_posts": BlogPost.objects.all()
    })

def blog_post(request,id):

    return render(request, "blog_app/blog_post.html",{
        "blog_post": BlogPost.objects.get(id=id)
    })
