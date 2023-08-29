from django.urls import path, include
from .views import LinuxDistributionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'distributions', LinuxDistributionViewSet)
urlpatterns = [
    path('api/', include(router.urls))
]
