from django.db import models
from django.db import models


class Myyja(models.Model):
    nimi = models.CharField(max_length=50, default='tyhja')
    titteli = models.CharField(max_length=50, default='titteli')
    puhelinnumero = models.CharField(max_length=20, default='00000000')
    email = models.EmailField(max_length=50, default='etu.suku@malli.fi')

    class Meta:
        ordering = ['nimi']

class Auto(models.Model):
    merkki = models.CharField(max_length=20, default='merkki')
    malli = models.CharField(max_length=20, default='malli')
    vuosimalli = models.IntegerField(default=2021)
    mittarilukema = models.IntegerField(default=0)
    vari = models.CharField(max_length=20, default='auton väri')
    hinta = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    myyja = models.ForeignKey(Myyja, on_delete=models.CASCADE)

    class Meta:
        ordering = ['hinta']