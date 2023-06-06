from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "slug", "body", "meta_description", "date_created", "date_modified", "publish_date", "published")

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)