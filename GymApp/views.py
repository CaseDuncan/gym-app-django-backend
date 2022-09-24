from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from GymApp.models import Service, Plan, Customer
from GymApp.serializers import ServiceSerializer, PlanSerializer, CustomerSerializer
# Create your views here.

@api_view(['GET','POST'])
def services_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def service_detail(request, pk):
    try:
        service = Service.objects.get(id = pk)
    except service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    elif request.nethod =='PATCH':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        service.delete()
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

#plans endpoints
@api_view(['GET', 'POST'])
def plans_list(request):
    if request.method =='GET':
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)
        
    elif request.method =='POST':
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
through these endpoints you can update, delete and retrieve a plan
"""
@api_view(['GET', 'PATCH', 'DELETE'])
def plans_details(request, pk):
    try:
        plan = Plan.objects.get(id =pk)
    except plan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = PlanSerializer(plan)
        return Response(serializer.data)
    
    elif request.method =='PATCH':
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#customer endpoints
@api_view(['GET','POST'])
def customer_list(request):
    if request.method =='GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
API endpoints for  updating, deleting and retrieving a customer
"""
@api_view(['GET', 'PATCH', 'DELETE'])
def customers_details(request, pk):
    try:
        customer = Customer.objects.get(id =pk)
    except customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = PlanSerializer(customer)
        return Response(serializer.data)
    
    elif request.method =='PATCH':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)