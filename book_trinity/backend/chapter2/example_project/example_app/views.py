#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
       return HttpResponse("Hello, World!")

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

