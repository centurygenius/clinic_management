from django.db import models
import uuid
class Patient(models.Model):
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=3, null=True)
    address = models.TextField(max_length=100, null=True)
    comment = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, null=True, choices=[('male', 'Male'), ('female', 'Female')])
    doctor_prescription = models.TextField(max_length=500, null=True)
    systolic = models.CharField(max_length=10, null=True)
    diastolic = models.CharField(max_length=10, null=True)
    temperature = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    nurse_name = models.CharField(max_length=100, null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    hospital_id = models.CharField(max_length=12, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        # Automatically generate a custom hospital ID if not already set
        if not self.hospital_id:
            self.hospital_id = self.generate_hospital_id()
        super().save(*args, **kwargs)

    def generate_hospital_id(self):
        # Custom logic for hospital ID generation
        prefix = "CENT"
        # Create a unique ID using a combination of the prefix and a short UUID
        unique_id = uuid.uuid4().hex[:6].upper()  # Take first 6 characters of UUID
        return f"{prefix}-{unique_id}"
    def __str__(self):
        return f'{self.last_name} {self.first_name}'