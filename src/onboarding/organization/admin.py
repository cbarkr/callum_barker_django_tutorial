from django.contrib import admin
from .models import Location, Organization, Office, Employee


admin.site.register(Location)
admin.site.register(Organization)
admin.site.register(Office)
admin.site.register(Employee)
