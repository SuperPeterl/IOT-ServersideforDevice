from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

    

from django.http import JsonResponse
from django.middleware import csrf

def getget(request):
    token = csrf.get_token(request)
    response_data = {'csrf_token': token}
    return JsonResponse(response_data)


@csrf_exempt
def postpost(request):
    if request.method == 'POST':
        # Get the integer value from the request
        value = request.POST.get('x')
        print("I GET POST wow")
        # Do something with the integer value
        # ...
        print("WOOWOWOWOWOWO",value)
        # Return a JSON response with a success message
        return JsonResponse({'success': True})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})