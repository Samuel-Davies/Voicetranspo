# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destination'

    


class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    time = models.ForeignKey('Time', models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, blank=True, null=True)
    destination = models.ForeignKey(Destination, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Time(models.Model):
    id = models.IntegerField(primary_key=True)
    departure = models.TimeField(blank=True, null=True)
    arrival = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time'


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=60, blank=True, null=True)
    color = models.CharField(max_length=60, blank=True, null=True)
    brand = models.CharField(max_length=60, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'
