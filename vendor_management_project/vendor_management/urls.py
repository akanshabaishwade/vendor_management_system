from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', views.PurchaseOrderListCreate.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('test_on_time_delivery_rate/<int:vendor_id>/', views.test_on_time_delivery_rate, name='test_on_time_delivery_rate'),
]
