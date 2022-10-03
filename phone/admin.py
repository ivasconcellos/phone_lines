from django.contrib import admin
from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'phone_type', 'department', 'sponsor', 'active', 'created_at', 'updated_at']
    search_fields = ['phone_number', 'phone_type', 'department', 'sponsor']

admin.site.register(Phone, PhoneAdmin)
