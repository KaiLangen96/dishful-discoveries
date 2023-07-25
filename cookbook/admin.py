"""Imports for admin page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Allows admin to manage categories via the admin panel
    """

    list_display = ('category', 'admin')


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage recipes via the admin panel
    """

    list_display = ('title', 'slug', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('created_on', 'updated_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Allows admin to manage comments on recipes via the admin panel
    """

    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
