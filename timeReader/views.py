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
from django.db.models import Avg, Sum
from django.utils import timezone
from datetime import date, datetime

import random
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
        if value >= 5*60*1000:
            tr = timeReader(timeReadedmilsec = value ,timeReadedsecond = value/1000 ,timeReadedminute = value/(60*1000))
            tr.save()

        # Return a JSON response with a success message
        return JsonResponse({'success': True})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def show(request):
    tms = timeReader.objects.all()
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
# Query the database for the average minutes per day
    results = timeReader.objects.filter(
            addDate__year=current_year,
            addDate__month = current_month,
            addDate__day = current_day)
    print(sum([x.timeReadedminute for x in results]))
# Print the results
    context  = {
        'tms':tms,
        'avg':sum([x.timeReadedminute for x in results])
    }
    return render(request,'index.html',context)


def fake(request):
    value = random.randint(60000,1800000)
    # Do something with the integer value
    if value >= 5*60*1000:
        tr = timeReader(timeReadedmilsec = value ,timeReadedsecond = value/1000 ,timeReadedminute = value/(60*1000))
        tr.save()
    return HttpResponse("faking")