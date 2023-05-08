from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ['name','created_by','created_at']
    search_fields=['name']
admin.site.register(Vendor ,VendorAdmin)
