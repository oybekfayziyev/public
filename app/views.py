from django.shortcuts import render
from rest_framework import viewsets
from app.models import Vehicle
from app.serializers import VehicleSerializer
from rest_framework import status;
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response 
# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all();
    serializer_class = VehicleSerializer
    print("serializer")
    @action(detail=True,methods=['post'])
    def update_data(self,request):
        print("here");
        vehicle = Vehicle.objects.all();
        serializer = VehicleSerializer(data=request.data);
        if serializer.is_valid():
            vehicle.save();
            return Response(status=status.HTTP_201_CREATED);
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST);
        
    
# @api_view(['GET','POST'])
# def vehicle_post(request):
#     try:
#         vehicle = Vehicle.objects.all();
#     except Vehicle.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND);
    
#     if request.method == 'GET':
#         serializer = VehicleSerializer(vehicle,many = True);
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = VehicleSerializer(vehicle,data = request.data);
#         if serializer.is_valid():
#             serializer.save();
#             return Response(serializer.data,status=status.HTTP_201_CREATED);
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    






