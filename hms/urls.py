from django.urls import path
from hms.views import (
    DoctorListView,
    PatientListView,
    PatientDetailsListView,
)


urlpatterns = [
    path(
        "doctor",
        DoctorListView.as_view(),
        name="doctor-list",
    ),
    path(
        "patients",
        PatientListView.as_view(),
        name="patients-list",
    ),
    path(
        "patients/<str:id>",
        PatientDetailsListView.as_view(),
        name="patients-list",
    ),
]
