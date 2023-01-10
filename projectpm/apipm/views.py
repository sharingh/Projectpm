from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Avg, Max, Min, Sum

from apipm.models import Measurers,Measurements
from apipm.serializers import MeasurerSerializer,MeasurementSerializer

@csrf_exempt
def apimsr(request,id=0):
    if request.method=='GET':
        measurers = Measurers.objects.all()
        measurers_serializer=MeasurerSerializer(measurers,many=True)
        return JsonResponse(measurers_serializer.data,safe=False)
    elif request.method=='PUT':
        measurer_data=JSONParser().parse(request)
        measurer=Measurers.objects.get(MeasurerId=measurer_data['MeasurerId'])
        measurers_serializer=MeasurerSerializer(measurer,data=measurer_data)
        if measurers_serializer.is_valid():
            measurers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        measurer=Measurers.objects.get(MeasurerId=id)
        measurer.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def apimsradd(request,id=0):
    if request.method=='GET':
        measurers = Measurers.objects.all()
        measurers_serializer=MeasurerSerializer(measurers,many=True)
        return JsonResponse(measurers_serializer.data,safe=False)
    elif request.method=='POST':
        measurer_data=JSONParser().parse(request)
        measurers_serializer=MeasurerSerializer(data=measurer_data)
        if measurers_serializer.is_valid():
            measurers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def apimsrsend(request,id=0):
    if request.method=='GET':
        measurements = Measurements.objects.all()
        measurements_serializer=MeasurementSerializer(measurements,many=True)
        return JsonResponse(measurements_serializer.data,safe=False)
    elif request.method=='POST':
        measurement_data = JSONParser().parse(request)
        con = float(measurement_data['MeasurementCo'])
        if con < 0:
            return JsonResponse("The measurement is discarded because the value is negative",safe=False)
        measurements_serializer=MeasurementSerializer(data=measurement_data)
        if measurements_serializer.is_valid():
            measurements_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

def apidatacon(request, id=0):
    if request.method == 'GET':
        conmax=Measurements.objects.filter(MeasurerId=id).aggregate(max_con=Max('MeasurementCo'), min_con=Min('MeasurementCo'), prom_con=Avg('MeasurementCo'), tot_con=Sum('MeasurementCo'))
        return JsonResponse(conmax,safe=False)

def apimaxcon(request, id=0):
    if request.method == 'GET':
        conmax=Measurements.objects.filter(MeasurerId=id).aggregate(max_con=Max('MeasurementCo'))
        return JsonResponse(conmax,safe=False)

def apimincon(request, id=0):
    if request.method == 'GET':
        conmax=Measurements.objects.filter(MeasurerId=id).aggregate(min_con=Min('MeasurementCo'))
        return JsonResponse(conmax,safe=False)

def apiavgcon(request, id=0):
    if request.method == 'GET':
        conmax=Measurements.objects.filter(MeasurerId=id).aggregate(avg_con=Avg('MeasurementCo'))
        return JsonResponse(conmax,safe=False)

def apitotcon(request, id=0):
    if request.method == 'GET':
        conmax=Measurements.objects.filter(MeasurerId=id).aggregate(tot_con=Sum('MeasurementCo'))
        return JsonResponse(conmax,safe=False)
