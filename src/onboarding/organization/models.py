from django.db import models
from django.conf import settings

class Location(models.Model):
    """
    Each Location may have many Organizations or Offices
    """
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.address}, {self.city}, {self.country}"


class Organization(models.Model):
    """
    Each Organization has only one location
    """
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Office(models.Model):
    """
    Each Office has only one location and belongs to only one organization
    """
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.organization.name} {self.name}"


class Employee(models.Model):
    """
    Each Employee works only in one office
    Note: Assumes that employees are employed by a specific office
    Note: Wording is unclear as to whether or not we are creating the Employee table itself
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"