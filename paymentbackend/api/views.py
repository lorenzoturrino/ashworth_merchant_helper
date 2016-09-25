from django.http import JsonResponse, HttpResponse


def quote(request):
    if request.method == 'POST':
        return JsonResponse({'foo':'bar'})
    else:
        return HttpResponse(status=405)