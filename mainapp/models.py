from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    emergency_contact = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
