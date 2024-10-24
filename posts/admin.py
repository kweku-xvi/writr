from .models import Blog
from django.contrib import admin


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Blog, BlogAdmin)