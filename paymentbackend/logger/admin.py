from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'amount', 'currency','method', 'transaction_fee', 'time']
    list_display = ['id', 'amount', 'currency', 'method', 'transaction_fee', 'time']
    actions = None