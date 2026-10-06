from django.db import models
from django.contrib import admin
class service_vehicles_details(models.Model):
    vehicle_no=models.CharField(max_length=10)
    owner_name=models.CharField(max_length=5)
    owner_mob_no1=models.IntegerField()
    owner_mob_no2=models.IntegerField()
    license_no=models.CharField(max_length=10,primary_key=True)
    date=models.DateField()
    fees_paid=models.CharField(max_length=10)
class service_vehicles_detailsAdmin(admin.ModelAdmin):
  list_display=["vehicle_no","owner_name","owner_mob_no1","owner_mob_no2","license_no","date","fees_paid"]

