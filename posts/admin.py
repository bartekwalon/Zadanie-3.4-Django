from django.contrib import admin
from posts.models import Post, Author


@admin.register(Author)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['nick', 'email', 'bio']
    list_filter = ['nick']
    search_fields = ['nick', 'email']


@admin.register(Post)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created', 'modified', 'author_id']
    list_filter = ['author_id']
