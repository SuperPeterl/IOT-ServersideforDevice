from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from timeReader.models import timeReader
from django.shortcuts import render
from django.utils import timezone
from .models import timeReader    
from datetime import timedelta
from django.http import JsonResponse
from django.middleware import csrf
from django.core import serializers
def getget(request):
    token = csrf.get_token(request)
    response_data = {'csrf_token': token}
    return JsonResponse(response_data)


@csrf_exempt
def postpost(request):
    if request.method == 'POST':
        # Get the integer value from the request
        value = request.POST.get('x')
        value = int(value)
        # Do something with the integer value
        tr = timeReader(timeReadedmilsec = value ,timeReadedsecond = value/1000 ,timeReadedminute = value/(60*1000)).create()
        tr.save()
        # Return a JSON response with a success message
        return JsonResponse({'success': True})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def show(request):
    tms = timeReader.objects.all()
    context  = {
        'tms':tms
    }
    return render(request,'index.html',context)
