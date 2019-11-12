from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import json


# Create your views here.
def showhuman(request):
    d1 = {
        'idno': 101,
        'name': 'Ravi',
        'salary': 185000.00
    }
    return render(request, 'index.html', d1)

def showapplication(request):
    d1 = {'idno': 101, 'name': 'Ravi', 'sal': 185000.00}
    #converting dict to json
    Json_data=json.dumps(d1)
    return HttpResponse(Json_data,content_type='application/json')


def showapp(request):
    return render()