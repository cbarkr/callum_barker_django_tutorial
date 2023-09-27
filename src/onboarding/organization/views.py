from .models import Organization, Office, Location, Employee
from .serializers import OfficeSerializer, OrganizationSerializer, LocationSerializer, EmployeeSerializer

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def index(request, format=None) -> Response:
    return Response({
        'organizations': reverse('organization-list', request=request, format=format),
    })


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer) -> None:
        serializer.save()


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def perform_create(self, serializer) -> None:
        serializer.save()


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer) -> None:
        serializer.save()


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer) -> None:
        serializer.save()