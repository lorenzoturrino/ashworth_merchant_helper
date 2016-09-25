from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json, os, requests

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
    rate = get_midmarket_rate(transaction.get('currency'))
    return JsonResponse({'suggested_method': rate})


def get_midmarket_rate(currency):
    XIGNITE_ENDPOINT = 'http://globalcurrencies.xignite.com/xGlobalCurrencies.json/GetRealTimeRate?Symbol=%sGBP&_token=%s'
    if currency == 'GBP':
        return 1.0
    else:
        market_rate = requests.get(XIGNITE_ENDPOINT % (currency, os.environ.get('XIGNITE_TOKEN'))).json()
        return market_rate.get('Mid')

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