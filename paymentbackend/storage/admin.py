from django.contrib import admin
from .models import Processor, ApiKey


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'description', 'base_rate', 'percentage_rate']
    list_display = ['name', 'active', 'base_rate', 'percentage_rate', 'description']
    list_editable = ['active',]


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    pass