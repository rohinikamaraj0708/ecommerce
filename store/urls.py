from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, create_order

router = DefaultRouter()

router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),

    # Razorpay payment order create API
    path("create-order/", create_order, name="create_order"),
]