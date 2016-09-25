from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['amount', 'method', 'transaction_fee', 'time']
    list_display = ['amount', 'method', 'transaction_fee', 'time']