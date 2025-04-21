from django.db import models

# Create your models here.
class UfrainRegistration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=False, unique=True)
    dob = models.DateField()
    phone_no = models.CharField(max_length=15)
    hight = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=10)
