# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from .models import Dogs,Types

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')
def flight(request):
    response = requests.get('http://host.docker.internal:8000/flights')
    result = response.json()
    cuantos = len(result['data'])
    return render(request, 'flights.html', {'cuantos': cuantos , 'flights': result})
    #return JsonResponse(result)
def flightget(request,id):
    response = requests.get('http://host.docker.internal:8000/flight/get/'+ str(id))
    result = response.json()
    return render(request, 'get.html', {'flight': result['data']})
    #return JsonResponse(result)

def flightupdate(request,id):
    response = requests.post('http://host.docker.internal:8000/flight/get',json.dumps({"id": id}))
    result = response.json()
    return render(request, 'update.html', {'flight': result['data']})

def flight_update(request,id):
    datos = request.POST
    response = requests.post('http://host.docker.internal:8000/flight/update/'+ str(id),  json = datos)
    return redirect("/get/"+ str(id))

def flightdelete(request,id):
    response = requests.delete('http://host.docker.internal:8000/flight/delete/'+ str(id))
    result = response.json()
    return redirect("/")
def flight_add(request):
    return render(request, 'add.html')

def flightadd(request):
    datos = request.POST
    response = requests.post('http://host.docker.internal:8000/flight/add',  json = datos)
    return redirect("/add")

def product(request):
    datos = request.POST
    response = requests.post('http://host.docker.internal:8000/',  json = datos)
    result = response.json()
    cuantos = len(result['data'])
    return render(request, 'flights.html', {'cuantos': cuantos , 'flights': result})
