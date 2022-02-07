from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .scripts.main import *
from django.shortcuts import render

# Create your views here.
def index(request):
    data = main()
#    return JsonResponse(data, safe = False)
    context = {'data':data} 
    return render(request, 'namespace.html', context)
