from rest_framework import serializers
from organization.models import Organization, Office, Location, Employee


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields: list[str] = ["address", "city", "province", "postal_code", "country"]


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.get_full_name")
    email = serializers.CharField(source="user.email")
    location = LocationSerializer()

    class Meta:
        model = Employee
        fields: list[str] = ["name", "email", "location"]


class OfficeSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = Office
        fields: list[str] = ["name", "location", "phone_no", "employees"]


class OrganizationSerializer(serializers.ModelSerializer):
    offices = OfficeSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = Organization
        fields: list[str] = ["name", "location", "phone_no", "offices"]
