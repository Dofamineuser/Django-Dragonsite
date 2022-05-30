from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(File, FileAdmin)
