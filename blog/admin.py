from django.contrib import admin
from .models import Post, Comment, Category, Tag, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Like)

