from django.db import models
class Customer(models.Model):
    Fullname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=40)
    Contact=models.CharField(max_length=50)
    Dob=models.CharField(max_length=40)
    Gender=models.CharField(max_length=10)
