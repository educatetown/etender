from django.contrib import admin

from django.contrib import admin
from .models import Others


class OthersAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'last_date']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Others, OthersAdmin)

