from django.urls import path, URLPattern, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'organization', views.OrganizationViewSet, basename="organization")
router.register(r'office', views.OfficeViewSet, basename="office")
router.register(r'location', views.LocationViewSet, basename="location")
router.register(r'employee', views.EmployeeViewSet, basename="employee")

urlpatterns: list[URLPattern] = [
    path('', include(router.urls)),
]
