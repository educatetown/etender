from django.contrib import admin

from django.contrib import admin
from .models import Intents2Awards


class I2AAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'last_date']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Intents2Awards, I2AAdmin)

