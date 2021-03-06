from django.db import models


class Transaction(models.Model):
    # original transaction
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.TextField(max_length=10)
    gbp_value = models.DecimalField(decimal_places=2, max_digits=10)

    # payment processor
    method = models.CharField(max_length=255)
    transaction_fee = models.DecimalField(decimal_places=2, max_digits=10)
    net_transaction = models.DecimalField(decimal_places=2, max_digits=10)

    # customer info
    card_brand = models.CharField(max_length=255, blank=True, null=True)
    card_issuer = models.CharField(max_length=255, blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    card_country = models.CharField(max_length=255, blank=True, null=True)

    #logging
    time = models.DateTimeField(auto_now=True)

    @property
    def fee_percentage(self):
        return '%.2f' % (self.transaction_fee / self.gbp_value * 100) + r'%'
