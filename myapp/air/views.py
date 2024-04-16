from django.shortcuts import render
from django.http import HttpResponse,request
from .models import *



def index(request):
    companies = Company.objects()
 
    return HttpResponse(companies)




# Create your views here.
