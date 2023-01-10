from rest_framework import serializers
from apipm.models import Measurers, Measurements

class MeasurerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Measurers
        fields=('MeasurerId','MeasurerName')

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Measurements
        fields=('MeasurementId','MeasurementDate','MeasurementCo','MeasurerId','MeasurerName')
