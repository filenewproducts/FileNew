from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bookClass(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)