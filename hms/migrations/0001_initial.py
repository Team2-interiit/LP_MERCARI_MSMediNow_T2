# Generated by Django 4.0.3 on 2022-03-24 18:04

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("did", models.CharField(blank=True, max_length=100)),
                ("speciality", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("nhid", models.CharField(max_length=30)),
                ("gender", models.CharField(blank=True, max_length=10)),
                ("age", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("phone_number", models.CharField(blank=True, max_length=10)),
                ("address", models.CharField(blank=True, max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicalRecords",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("image_url", models.URLField(blank=True, null=True)),
                ("report_type", models.CharField(blank=True, max_length=50)),
                ("issued_at", models.DateTimeField(auto_now_add=True)),
                ("comments", models.TextField()),
                (
                    "issued_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prescriptions",
                        to="hms.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="records",
                        to="hms.patient",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="hospital",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctors",
                to="hms.hospital",
            ),
        ),
    ]
