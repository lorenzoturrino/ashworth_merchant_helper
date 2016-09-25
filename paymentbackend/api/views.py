from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json

from storage.models import Processor
from logger.models import Transaction


@csrf_exempt
def best_quote(request):  # returns the best payment method. Expects a transaction_value:value key pair via POST
    if request.method == 'POST':
        transaction = json.loads(request.body)
        if transaction.get('value') and transaction.get('currency'):
            return process_quote(transaction)
        else:
            return HttpResponse('Missing required parameter', status=400)
    return HttpResponse('This endpoint only accepts POST requests', status=405)


def index(request):  # just a landing page
    return HttpResponse('This is the Ashworth quoting service v1 API. Have fun.', status=200)


def process_quote(transaction):
    pass

# def process_quote(transaction_value):
#     min_commission = float('inf')
#     best_method = None
#     for psp in Processor.objects.all():
#         if psp.transaction_cost(transaction_value) < min_commission:
#             best_method = psp.name
#             min_commission = psp.transaction_cost(transaction_value)
#     log_transaction(transaction_value, min_commission, best_method)
#     return JsonResponse({'suggested_method': best_method})


def log_transaction(value, commission, method):
    log_entry = Transaction(
        amount=value,
        method=method,
        transaction_fee=commission,
    )
    log_entry.save()