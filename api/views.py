import json 
import requests
import geopy.distance
from django.shortcuts import render, redirect
from django.db.models import Q


from rest_framework import generics
from .models import *
from .serializers import DistanceSerializer

class ListGeneric(generics.ListCreateAPIView):
    serializer_class = DistanceSerializer
    queryset = Distance.objects.all()

def doSearch(type_of_add, request):
    url = "https://nominatim.openstreetmap.org/search?format=geojson"

    add = Address()

    type_of_add = type_of_add + '_'

    if type_of_add+'number' in request and type_of_add+'street' in request:
        add.number =  request[type_of_add+'number']
        add.street =  request[type_of_add+'street']
        url = url + '&' + 'street=' + request[type_of_add+'number'] + ' ' + request[type_of_add+'street']

    elif type_of_add+'number' in request:
        add.number =  request[type_of_add+'number']
        url = url + '&' + 'street=' + request[type_of_add+'number']

    elif type_of_add+'street' in request:
        add.street =  request[type_of_add+'street']
        url = url + '&' + 'street=' + request[type_of_add+'street']
    

    if type_of_add+'city' in request:
        add.city =  request[type_of_add+'city']
        url = url + '&' +'city='+ request[type_of_add+'city']
    
    if type_of_add+'county' in request:
        add.county =  request[type_of_add+'county']
        url = url + '&' +'county='+ request[type_of_add+'county']
    
    if type_of_add+'state' in request:
        add.state =  request[type_of_add+'state']
        url = url + '&' +'state='+ request[type_of_add+'state']
    
    if type_of_add+'country' in request:
        add.country =  request[type_of_add+'country']
        url = url + '&' +'country='+ request[type_of_add+'country']
    
    if type_of_add+'postalcode' in request:
        add.postalcode =  request[type_of_add+'postalcode']
        url = url + '&' +'postalcode='+ request[type_of_add+'postalcode']

    response = requests.request("GET", url, headers={}, data={})
    json_response = json.loads(response.text)    
    coordinates = None

    if len(json_response['features']) > 1:
        coordinates = json_response['features'][0]['geometry']['coordinates']

    add.save()
    return add, coordinates

def calcuteDistance(source, destination):
    return geopy.distance.geodesic(source, destination).km

def search(request):
    serializer_class = DistanceSerializer
    distance = None
    message = None

    if request.method == 'POST':
        source, source_coordinates = doSearch('source',request.POST)
        destination, destination_coordinates = doSearch('destination',request.POST)
        print(destination_coordinates)

        if source_coordinates is not None and destination_coordinates is not None:
            distance = calcuteDistance(source_coordinates, destination_coordinates)
            search = Distance()
            search.source = source
            search.destination = destination
            search.distance = distance 
            search.save()
        else:
            message = 'There has been an error during the calculation, please retry it in a few moments'
    

    return render(request, 'search.html',{'distance':distance, 'message':message})

def history(request):
    distances = Distance.objects.all()
    return render(request, 'history.html', { 'distances':distances})