from uuid import uuid4

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Hospital(models.Model):
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    did = models.CharField(max_length=100, blank=True)
    speciality = models.CharField(max_length=100)
    hospital = models.ForeignKey(
        Hospital, related_name="doctors", on_delete=models.CASCADE, blank=True
    )

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, blank=True, null=True)
    user = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)
    nhid = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nhid


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()


# ? Reports, prescriptions, etc
class MedicalRecords(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, related_name="records", on_delete=models.CASCADE
    )
    image_url = models.URLField(blank=True, null=True)
    report_type = models.CharField(max_length=50, blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    issued_by = models.ForeignKey(
        Doctor, related_name="prescriptions", on_delete=models.CASCADE
    )
    comments = models.TextField()
