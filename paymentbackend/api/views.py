from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from storage.models import Processor


@csrf_exempt
def best_quote(request):  # returns the best payment method. Expects a transaction_value:value key pair via POST
    if request.method == 'POST':
        transaction_value = float(request.POST.get('transaction_value'))
        if transaction_value:
            min_commission = float('inf')
            best_method = None
            for psp in Processor.objects.all():
                if psp.transaction_cost(transaction_value) < min_commission:
                    best_method = psp.name
                    min_commission = psp.transaction_cost(transaction_value)
            return JsonResponse({'suggested_method':best_method})
        return HttpResponse('Missing required parameter', status=400)
    return HttpResponse('This endpoint only accepts POST requests', status=405)


def index(request):  # just a landing page
    return HttpResponse('This is the Ashworth quoting service v1 API. Have fun.', status=200)