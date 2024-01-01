from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    """
    - accepts  request parameter which is passed automatically via django
    - returns an HttpResponse() object instance imported from django - see line 2
    - pass the response data to the HttpResponse() instance which could be a string or an html file
    """
    return HttpResponse("Eat no meat for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
