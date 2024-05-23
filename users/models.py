from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    MALE = "male"
    FEMALE = "female"
    UNGENDER = "ungender"
    TYPE_GENDER=(
        (MALE, "Hombre"),
        (FEMALE, "Mujer"),
        (UNGENDER, "No definido"),
    )
    street = models.CharField(max_length=100, blank=True, null=True)
    colony = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    external_number = models.CharField(max_length=5, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=TYPE_GENDER, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)