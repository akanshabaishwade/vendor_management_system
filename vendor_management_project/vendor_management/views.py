from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from django.utils import timezone
from django.http import JsonResponse


class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'


def test_on_time_delivery_rate(request, vendor_id):

    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return JsonResponse({'error': 'Vendor not found'}, status=404)

    # Create two dummy PurchaseOrder objects with different delivery dates
    po1 = PurchaseOrder.objects.create(
        po_number="PO909",
        vendor=vendor,
        order_date=timezone.now(),  # Set the order date to the current date/time
        delivery_date=timezone.now(),  # Set the delivery date to the current date/time
        items={"item1": "details1", "item2": "details2"},  # Example items
        quantity=10,  # Example quantity
        status="completed",  # Example status
        quality_rating=4.5,  # Example quality rating
        issue_date=timezone.now(),  # Set the issue date to the current date/time
        acknowledgment_date=timezone.now()  # Set the acknowledgment date to the current date/time
    )
    po2 = PurchaseOrder.objects.create(
        po_number="PO908",  # Unique po_number
        vendor=vendor,
        order_date=timezone.now(),  # Set the order date to the current date/time
        delivery_date=timezone.now() - timezone.timedelta(days=1),  # One day ago
        items={"item1": "details1", "item2": "details2"},  # Example items
        quantity=10,  # Example quantity
        status="completed",  # Example status
        quality_rating=4.5,  # Example quality rating
        issue_date=timezone.now(),  # Set the issue date to the current date/time
        acknowledgment_date=timezone.now()  # Set the acknowledgment date to the current date/time
    )
    # Update the on-time delivery rate
    vendor.update_performance_metrics()

    # Return the vendor's on_time_delivery_rate as a response
    return JsonResponse({'on_time_delivery_rate': vendor.on_time_delivery_rate})
