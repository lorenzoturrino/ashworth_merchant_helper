from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'amount', 'currency', 'gbp_value', 'method', 'transaction_fee', 'net_transaction', 'time',
                       'fee_percentage', 'card_brand', 'card_type', 'card_country', 'card_issuer']
    list_display = ['id', 'time', 'amount', 'currency', 'net_transaction', 'method', ]
    fieldsets = [
        (None, {
            'fields': (('id', 'time'),)
        }),
        ('Transaction', {
            'fields': (('amount', 'currency'), ('gbp_value','net_transaction')),
        }),
        ('Payment Processor', {
            'fields': (('method', 'transaction_fee', 'fee_percentage'),),
        }),
        ('Customer', {
            'fields': (('card_brand', 'card_type', 'card_country', 'card_issuer'),),
        }),
    ]

    actions = None