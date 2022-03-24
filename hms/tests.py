from django.test import TestCase
from hms.models import Hospital


class HospitalTestCase(TestCase):
    def testHospital(self):
        hospital = Hospital(location="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(hospital.title, "My Title")
        self.assertEqual(hospital.description, "Blurb")
        self.assertEqual(hospital.wiki, "Hospital Body")


# Create your tests here.
