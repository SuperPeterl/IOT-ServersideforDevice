from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        # Process the POST request data
        data = request.POST.get('data')
        # Store the data in the database or perform some other action
        return HttpResponse('Data received')
    else:
        return HttpResponse('Invalid request method')
    

def getget(request):
    print('i get get')
    response = HttpResponse(status=200)
    return response