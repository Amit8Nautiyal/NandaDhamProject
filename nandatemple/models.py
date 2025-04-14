from django.db import models

# Create your models here.
class Registration(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    total_person = models.IntegerField()
    email = models.EmailField(max_length=254)
