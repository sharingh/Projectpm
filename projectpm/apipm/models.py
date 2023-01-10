from django.db import models

class Measurers(models.Model):
    MeasurerId = models.AutoField(primary_key=True)
    MeasurerName = models.CharField(max_length=50)

class Measurements(models.Model):
    MeasurementId = models.AutoField(primary_key=True)
    MeasurementDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    MeasurementCo = models.DecimalField(max_digits=10, decimal_places=2)
    MeasurerId = models.CharField(max_length=50)
    MeasurerName = models.CharField(max_length=50)
