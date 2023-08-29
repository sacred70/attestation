from django.urls import path, include
from rest_framework import routers
from commercial_network.views import SupplierViewSet, NetworkViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

