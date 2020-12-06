from django.contrib import admin

from django.contrib import admin
from .models import Proposal


class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'last_date']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Proposal, ProposalAdmin)

