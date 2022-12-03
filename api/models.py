from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)


# Create your models here.

class BloodBankDonor(models.Model):
    quantity_available=models.FloatField()
    b_manager=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    address=models.TextField(max_length=300)
    b_name=models.CharField(max_length=100)

class Donor(models.Model):
    dname = models.CharField(max_length=100)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
        ("Others","others"),
    ]
    gender = models.CharField(
        max_length=6,choices=gender_choices,
        )
    dob = models.DateField()
    blood_choices=[
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
 
    ]
    blood_group = models.CharField(
        max_length=4,
        choices=blood_choices
        )
    phoneno = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    weight = models.IntegerField()
    class_name_choices=(
        ("csa","CSA"),
        ("csb","CSB"),
        ("eca","ECA"),
        ("ecb","ECB"),
        ("eee","EEE"),
        ("mech","MECH"),
        ("eb","EB"),
    )
    class_name= models.CharField(max_length=4,choices=class_name_choices)
    batch_choices = (
        ("2023","2023"),
        ("2024","2024"),
        ("2025","2025"),
        ("2026","2026"),
    )
    batch = models.CharField(max_length=4,choices=batch_choices)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    last_donated_date = models.DateField()
    diseases = models.CharField(max_length=1000)
    allergies_choices = (
        ("yes","Yes"),
        ("no","No"),
    )
    allergies = models.CharField(max_length=3,choices=allergies_choices)
    cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        )
    bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        )
    hiv_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    hiv =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hiv_choices,
        )
    hepatitis_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    hepatitis =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hepatitis_choices,
        )
    def __str__(self):
        return self.dname

