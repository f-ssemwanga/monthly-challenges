from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    - accepts  request parameter which is passed automatically via django
    - returns an HttpResponse() object instance imported from django - see line 2
    - pass the response data to the HttpResponse() instance which could be a string or an html file
    """
    return HttpResponse("Jan Works!")


def feb(request):
    return HttpResponse("Feb Now work!")
