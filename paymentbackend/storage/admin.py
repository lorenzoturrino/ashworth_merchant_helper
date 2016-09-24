from django.contrib import admin
from .models import Processor, ApiKey


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'description']


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    pass