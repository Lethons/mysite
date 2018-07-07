from django.contrib import admin
from .models import Tag, Blog, SublimtMessage


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_per_page = 20


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'publish_time', 'update_time', 'is_commend')
    list_editable = ['is_commend',]
    list_per_page = 20


@admin.register(SublimtMessage)
class SublimtMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'publish_time', 'is_show')
    list_editable = ['is_show',]
    list_per_page = 20
