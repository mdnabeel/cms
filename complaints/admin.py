from django.contrib import admin
from .models import Station, Status, Department, FaultDetail, StatusFilter, DepartmentFilter, StationFilter
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export import resources, fields
from import_export.formats import base_formats
# Register your models here.


class FaultDetailResource(resources.ModelResource, ExportMixin):
    class Meta:
        model = FaultDetail
        export_order = ('id', 'station', 'department',
                        'fault_no', 'fault_description', 'fault_date',
                        'date_of_report', 'status', 'date_of_rectification',
                        'remarks')
        #fields = ('station', 'department', 'status',)
        #exclude = ('fault_no')


class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('dep_name',)
    search_fields = ['dep_name']

    def has_module_permission(self, request):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


class StationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

    def has_module_permission(self, request):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


class StatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cur_status',)
    search_fields = ['cur_status']

    def has_module_permission(self, request):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


class FaultDetailAdmin(ImportExportModelAdmin, ExportMixin,  admin.ModelAdmin):
    list_display = ('station', 'department',
                    'fault_description', 'fault_date', 'status', 'date_of_rectification')

    list_filter = [StatusFilter, DepartmentFilter, StationFilter]

    list_display_links = None

    list_editable = ('status', 'date_of_rectification')

    search_fields = ('fault_no', 'station__name', 'status__cur_status', 'fault_description')


    def has_import_permission(self, request):
        return False

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX
        )
        return [f for f in formats if f().can_export()]

    resource_class = FaultDetailResource


admin.site.register(Station, StationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(FaultDetail, FaultDetailAdmin)
