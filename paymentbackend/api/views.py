from django.http import JsonResponse, HttpResponse
from storage.models import Processor

def best_quote(request):
    if request.method == 'POST':
        min_commission = float('inf')
        best_method = None
        for psp in Processor.objects.all():
            if psp.transaction_cost(20) < min_commission:
                best_method = psp.name
        return JsonResponse({'suggested_method':best_method})
    else:
        return HttpResponse("This endpoint only accepts POST requests", status=405)

def index(request):
    return HttpResponse('This is the Ashworth quoting service v1 API. Have fun.', status=200)