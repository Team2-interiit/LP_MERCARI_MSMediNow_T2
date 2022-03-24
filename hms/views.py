from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Image, Doctor, Patient
from .serializer import MinDoctorSerializer, PatientSerializer


def image_upload(request):
    if request.method == "POST":
        image_file = request.FILES["image_file"]

        if settings.USE_S3:
            upload = Image(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return Response({"valid": True, "url": image_url})
    return Response({"valid": True, "url": image_url})


class DoctorListView(ListAPIView):
    serializer_class = MinDoctorSerializer
    queryset = Doctor.objects.all()


class PatientListView(ListAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientDetailsListView(ListAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = "id"
