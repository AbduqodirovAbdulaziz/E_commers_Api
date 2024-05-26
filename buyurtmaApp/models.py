from django.db import models
from mahsulotApp.models import Mahsulot
from userApp.models import User
from coreApp.models import CoreModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Sevimli(CoreModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "mahsulot"),)


class Savat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SavatMahsulot(CoreModel):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)


class Buyurtma(CoreModel):
    HOLAT_CHOICES = (
        ("Yigilmoqda", "Yigilmoqda"),
        ("Yetkazilmoqda", "Yetkazilmoqda"),
        ("Topshirdi", "Topshirdi"),
    )
    TOLOV_TURI = (
        ("Naqd", "Naqd"),
        ("Karta", "Karta"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    holat = models.CharField(max_length=25, choices=HOLAT_CHOICES, default="Yigilmoqda")
    tolov_turi = models.CharField(max_length=25, choices=TOLOV_TURI, default="Naqd")
    qoshimcha_tel = models.CharField(max_length=14)
    izoh = models.TextField(blank=True, null=True)
    manzil = models.TextField()
    summa = models.FloatField(default=0)


class BuyurtmaMahsulot(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)
