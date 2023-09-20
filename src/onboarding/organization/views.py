from django.views import generic
from .models import Organization


class IndexView(generic.ListView):
    template_name = "organization/index.html"
    context_object_name: str = "organization_list"

    def get_queryset(self):
        """Return all organizations, offices, and employees"""
        return Organization.objects.all()