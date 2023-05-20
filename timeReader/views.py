from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import status
from datetime import timedelta
from django.http import JsonResponse
from django.middleware import csrf
from django.db.models import Avg, Sum
from django.utils import timezone
from datetime import date, datetime
import random

def show(request):
    context = {}
    return render(request,'index.html',context)


def fake(request):
    status
    return HttpResponse("faking")

def listen(request):
    st = status.objects.filter(listened = 0)
    if len(st) > 0:
        res = ','.join([x.stid for x in st])
        for i in st:
            i.listened = 1
            i.save()
        print(res)
        return HttpResponse(res)
    return HttpResponse()

def order(request):
    value = request.POST.get('value')
    st = status(stid = value)
    st.save()
    context = {}
    return render(request,'index.html',context)