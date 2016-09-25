from django.db import models


class Transaction(models.Model):
    # original transaction
    amount = models.FloatField()
    currency = models.TextField(max_length=10)
    gbp_value = models.FloatField()

    # payment processor
    method = models.CharField(max_length=255)
    transaction_fee = models.FloatField()
    net_transaction = models.FloatField()

    #logging
    time = models.DateTimeField(auto_now=True)

    @property
    def fee_percentage(self):
        pass
        # return self.transaction_fee /