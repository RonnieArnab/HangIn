from django.db import models

# Create your models here.

class Date(models.Model):
  rec_date=models.DateField("date",blank=True)


class Time(models.Model):
  rec_time=models.TimeField("time",blank=True)


class footfall(models.Model):
  footfall_data=models.IntegerField("default=0")
