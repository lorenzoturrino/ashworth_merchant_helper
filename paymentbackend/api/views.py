from django.http import JsonResponse, HttpResponse


def best_quote(request):
    if request.method == 'POST':
        return JsonResponse({'foo':'bar'})
    else:
        return HttpResponse(status=405)

def index(request):
    return HttpResponse('This is the Ashworth quoting service v1 API. Have fun.')