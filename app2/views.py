from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_function(request):
    return HttpResponse('This App2 Function')