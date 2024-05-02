from django.db import models
from django.utils import timezone
from django.db.models import Avg, ExpressionWrapper, F, DurationField


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def update_performance_metrics(self):
        # Calculate On-Time Delivery Rate
        completed_orders = self.purchase_orders.filter(status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
        self.on_time_delivery_rate = on_time_orders.count() / completed_orders.count() * 100 if completed_orders.count() > 0 else 0

        # Calculate Quality Rating Average
        quality_ratings = completed_orders.exclude(quality_rating__isnull=True)
        self.quality_rating_avg = quality_ratings.aggregate(quality_rating_avg=Avg('quality_rating'))['quality_rating_avg'] if quality_ratings.count() > 0 else None

        # Calculate Average Response Time
        response_times = completed_orders.exclude(acknowledgment_date__isnull=True)
        self.average_response_time = response_times.aggregate(avg_response_time=Avg(ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())))['avg_response_time'].total_seconds() if response_times.count() > 0 else None

        # Calculate Fulfillment Rate
        self.fulfillment_rate = completed_orders.count() / self.purchase_orders.count() * 100 if self.purchase_orders.count() > 0 else 0

        # Save the updated metrics
        self.save()

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        # Update vendor's performance metrics if a completed PO is saved
        if not is_new and self.status == 'completed':
            self.vendor.update_performance_metrics()

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"

    class Meta:
        ordering = ['-date']
        verbose_name = 'Historical Performance'
        verbose_name_plural = 'Historical Performances'
