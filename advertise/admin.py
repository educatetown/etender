from django.contrib import admin
from .models import AdvertisingInfo, Advertising


class AdvertisingInfoAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['name', 'contact_no', 'banner_size', 'timestamp']
    search_fields = ['name']
    readonly_fields = ['timestamp', 'updated']
    list_filter = ['banner_size', 'timestamp']


class AdvertisingAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['title', 'active', 'timestamp', 'banner_size', 'choose_place']
    search_fields = ['title']
    list_editable = ['active', 'banner_size', 'choose_place']
    readonly_fields = ['timestamp', 'updated']
    list_filter = ['active', 'timestamp']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(AdvertisingInfo, AdvertisingInfoAdmin)
admin.site.register(Advertising, AdvertisingAdmin)

