from django.db import models
from django.utils import timezone
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class StationFilter(AutocompleteFilter):
    title = 'Stations'
    field_name = 'station'


class Department(models.Model):
    dep_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.dep_name


class DepartmentFilter(AutocompleteFilter):
    title = 'Department'
    field_name = 'department'


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"

    cur_status = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.cur_status


class StatusFilter(AutocompleteFilter):
    title = 'Fault Status'
    field_name = 'status'


class FaultDetail(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    fault_no = models.IntegerField()
    fault_description = models.TextField(default='')
    fault_date = models.DateField()
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE)
    date_of_rectification = models.DateField(blank=True, null=True)
    remarks = models.CharField(default='', max_length=255, blank=True)
    date_of_report = models.DateTimeField(default=timezone.now)
