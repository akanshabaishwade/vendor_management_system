from django.test import TestCase
from django.utils import timezone
from .models import Vendor, PurchaseOrder

class VendorPerformanceTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Vendor 1",
            contact_details="Contact details",
            address="Address",
            vendor_code="V001"
        )
        # Create dummy PurchaseOrder objects with different delivery dates and statuses
        PurchaseOrder.objects.create(
            vendor=self.vendor,
            delivery_date=timezone.now(),  # Assuming delivery date is now
            status="completed"
        )
        PurchaseOrder.objects.create(
            vendor=self.vendor,
            delivery_date=timezone.now() - timezone.timedelta(days=1),  # One day ago
            status="completed"
        )

    def test_on_time_delivery_rate_calculation(self):
        # Create two dummy PurchaseOrder objects with different delivery dates
        po1 = PurchaseOrder.objects.create(
            vendor=self.vendor,
            delivery_date=timezone.now(),  # Assuming delivery date is now
            status="completed"
        )
        po2 = PurchaseOrder.objects.create(
            vendor=self.vendor,
            delivery_date=timezone.now() - timezone.timedelta(days=1),  # One day ago
            status="completed"
        )

        # Update the on-time delivery rate
        self.vendor.update_delivery_rate()

        # Check the calculated rate
        # Assuming that update_delivery_rate sets the on_time_delivery_rate attribute
        self.assertEqual(self.vendor.on_time_delivery_rate, 0.5)  # 50% on-time delivery rate

        # Alternatively, you can check the value directly from the database
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.on_time_delivery_rate, 0.5)  # 50% on-time delivery rate
