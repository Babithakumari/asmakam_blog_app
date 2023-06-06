from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_post_all, name="blog_post_all"),
    path("blog_post/<int:id>", views.blog_post, name="blog_post")
]
