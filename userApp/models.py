from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    JINS_CHOICES = (
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol"),
    )
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Regular", "Regular"),
    )
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=14)
    rasm = models.ImageField(upload_to='users/', blank=True, null=True)
    manzil = models.TextField(blank=True, null=True)
    jins = models.CharField(max_length=20, choices=JINS_CHOICES, blank=True, null=True)
    t_sana = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES,default="Regular")

    def __str__(self):
        return self.username
