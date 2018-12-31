from django.http import JsonResponse


def health(request):
    json_msg = {'health': 'good'}
    return JsonResponse(json_msg)
