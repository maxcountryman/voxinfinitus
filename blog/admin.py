from django.contrib import admin
from .models import Author, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'slug', 'author', 'body', 'date_published',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
