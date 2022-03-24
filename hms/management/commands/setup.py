from django.contrib.auth import get_user_model
from django.core import management
from django.core.management.base import BaseCommand

from hms.models import Patient

User = get_user_model()

class Command(BaseCommand):
    help = "Migrates, loades data, downloads resources, and creates superuser"

    def add_arguments(self, parser):
        parser.add_argument("data-dir", nargs=1)
        parser.add_argument(
            "-o", "--offline", action="store_true", help="Avoid downloading resources."
        )

    def handle(self, *args, **options):
        management.call_command("migrate")
        management.call_command("collectstatic")
        management.call_command("createsuperuser")
        self.create_admin_profile()

        data_dir = options["data-dir"][0]
        is_offline = options["offline"]

        management.call_command("loadcoursesdata", data_dir)
        management.call_command("loadreviews", data_dir)

        if is_offline:
            management.call_command("downloadresources", data_dir)
        else:
            print("------- Skipping downloading resources.")

