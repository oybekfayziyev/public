from rest_framework import serializers;
from app.models import Vehicle;

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','vin','year','make','model','typev','color','dimensions','weight']
        
        # read_only_fields = ['year','make','model','typev','color','dimensions','weight']

      
            







