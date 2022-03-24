from django.contrib import admin
from .models import (
    Doctor,
    Hospital,
    Image,
    MedicalRecords,
    Patient,
)


class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number")


class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ("id", "patient")


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Image)
admin.site.register(MedicalRecords, MedicalRecordsAdmin)
