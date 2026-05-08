from django.core.validators import MinValueValidator
from django.db import models


class BookAppointment(models.Model):
    APPOINTMENT_CHOICES = [
        ("General", "General"),
        ("Dental", "Dental"),
        ("Skin", "Skin"),
        ("Heart", "Heart"),
        ("Other", "Other"),
    ]
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=55)
    phone = models.CharField(blank=False, max_length=20)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False, max_length=12)
    type_of = models.CharField(choices=APPOINTMENT_CHOICES, default="General")
    people = models.IntegerField(blank=False, validators=[MinValueValidator(1)], null=False)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Qrcode(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=55)
    phone = models.CharField(blank=False, max_length=20)
    date = models.CharField(blank=False, max_length=15)
    time = models.CharField(blank=False, max_length=12)
    people = models.IntegerField(blank=False, null=False)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name
