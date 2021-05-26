from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.


class KampeerSpot(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    info_text = models.CharField(max_length=200)
    camp_date = models.DateTimeField('Kampeerdatum')