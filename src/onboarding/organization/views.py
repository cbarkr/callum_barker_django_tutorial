from typing import Any
from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from django.core.serializers import serialize
from .models import Organization


def index(request) -> JsonResponse:
    organizations = Organization.objects.all()
    organizations_json = serialize("json", organizations)
    return JsonResponse(organizations_json, safe=False)


def detail(request, id) -> JsonResponse:
    """
    Get organization by ID, return it's name, phone_no, location, offices, and employees of each office

    Queries: 5
    """
    organization: Organization | None = (
        Organization.objects.filter(pk=id)
        .select_related("location")  # Select organization location
        .prefetch_related("offices", "offices__employees")  # Prefetch organization offices and employees
        .first()  # first() is slower than [0] or [:1] but it swallows exceptions for us
    )

    if organization:
        offices_list = []

        offices = organization.offices.select_related("location").all()

        for office in offices:
            employees = office.employees.select_related("user").all()

            # Add employee names and emails to office employee list
            office_employees_dict: dict[str, dict[str, Any]] = {
                "employees": [
                    {"name": str(e), "email": e.user.email}
                    for e in employees
                ]
            }

            # Get office info as a dict, exclude IDs
            office_dict: dict[str, Any] = model_to_dict(
                office, exclude=["id", "location", "organization"]
            )

            # Get office location as a dict, exclude IDs
            office_location_dict: dict[str, Any] = model_to_dict(
                office.location, exclude=["id"]
            )

            # Shallow merge dictionaries and add them to the office list
            offices_list.append(
                office_dict | office_employees_dict | office_location_dict
            )

        # Get organization info as a dict, exclude IDs
        organization_dict: dict[str, Any] = model_to_dict(
            organization, exclude=["id", "location"]
        )

        # Get organization location as a dict, exclude IDs
        organization_location_dict: dict[str, Any] = model_to_dict(
            organization.location, exclude=["id"]
        )

        # Get organization offices as a dict, exclude IDs
        organization_offices_dict: dict[str, Any] = {"offices": offices_list}

        # Return shallow merged dictionaries as JSON
        return JsonResponse(
            organization_dict | organization_location_dict | organization_offices_dict
        )

    raise Http404(f"Organization with id {id} does not exist")
