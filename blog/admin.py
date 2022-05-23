from django.contrib import admin
from .models import Blog, BlogCat


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'month')
    list_filter = ('organizer', 'month')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCat)
