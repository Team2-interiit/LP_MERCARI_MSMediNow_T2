from rest_framework import serializers
from .models import Doctor, MedicalRecords, Patient


class MinMedicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecords
        fields = ("id", "report_type", "image_url")


class MinDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("name", "speciality", "hospital")


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            "id",
            "name",
            "user",
            "nhid",
            "gender",
            "age",
            "phone_number",
            "address",
        )
