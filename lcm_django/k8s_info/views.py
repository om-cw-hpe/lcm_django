from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .scripts.main import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
'''def index(request):
    data = main()
#    return JsonResponse(data, safe = False)
    context = {'data':data} 
    return render(request, 'namespace.html', context)
'''
def nodes(request):
    data = get_nodes()
#    return JsonResponse(data, safe = False)
    context = {'data':data} 
    return render(request, 'namespace.html', context)
'''
class ReactView(APIView):
    def get(self, request):
        data = get_nodes()
        return Response(data)'''
