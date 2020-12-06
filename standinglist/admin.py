from django.contrib import admin

from django.contrib import admin
from .models import StandingList


class StandingListAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'last_date']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(StandingList, StandingListAdmin)

