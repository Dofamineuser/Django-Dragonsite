from django.contrib import admin
from .models import *

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


admin.site.register(Team, TeamAdmin)
admin.site.register(OwnerInfo)

