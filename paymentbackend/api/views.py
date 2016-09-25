from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json, os, requests

from storage.models import Processor
from logger.models import Transaction


@csrf_exempt
def best_quote(request):  # returns the best payment method. Expects a json-encoded string of params.
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
    if(transaction.get('cardNumber')):
        card_details = get_card_details(transaction.get('cardNumber'))
    else:
        card_details = {}
    midmarket_rate = get_midmarket_rate(transaction.get('currency'))
    transaction_value = transaction.get('value')
    min_commission = float('inf')
    best_method = None
    for psp in Processor.objects.all():  # processing a query with a for loop. this will become a queryset.
        if psp.transaction_cost(transaction_value, midmarket_rate) < min_commission:
            best_method = psp.name
            min_commission = psp.transaction_cost(transaction_value, midmarket_rate)
    log_transaction(transaction_value, min_commission, best_method, transaction.get('currency'), midmarket_rate, card_details)
    return JsonResponse({'best_method': best_method})


def get_midmarket_rate(currency):
    XIGNITE_ENDPOINT = 'http://globalcurrencies.xignite.com/xGlobalCurrencies.json/GetRealTimeRate?Symbol=%sGBP&_token=%s'
    if currency == 'GBP':
        return 1.0
    else:
        market_rate = requests.get(XIGNITE_ENDPOINT % (currency, os.environ.get('XIGNITE_TOKEN'))).json()
        return market_rate.get('Mid')

def get_card_details(card_number):
    BINLIST_ENDPOINT = 'https://binlist.net/json/%s'
    return requests.get(BINLIST_ENDPOINT % card_number).json()

def log_transaction(value, commission, method, currency, midmarket, card_details):
    gbp_value = value * midmarket
    log_entry = Transaction(
        amount=value,
        currency=currency,
        gbp_value=gbp_value,

        method=method,
        transaction_fee=commission,
        net_transaction=gbp_value-commission,

        card_brand=card_details.get('brand'),
        card_issuer=card_details.get('bank'),
        card_type=card_details.get('card_type'),
        card_country=card_details.get('country_code'),
    )
    log_entry.save()