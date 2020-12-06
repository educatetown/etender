from django.contrib import admin
from .models import Tender, PricingClientInfo
# u/p   >>tp/tp


class TenderAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'last_date']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Tender, TenderAdmin)
admin.site.register(PricingClientInfo)

