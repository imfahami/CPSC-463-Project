from django.db import models


# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.DateField(max_length=8)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)
    sex = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


