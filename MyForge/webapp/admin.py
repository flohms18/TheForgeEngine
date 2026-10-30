from django.contrib import admin
from .models import Post, Tag, Project

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Project)