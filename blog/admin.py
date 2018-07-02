from django.contrib import admin
from .models import Tag, Blog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_per_page = 20


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'publish_time', 'is_commend')
    list_per_page = 20
