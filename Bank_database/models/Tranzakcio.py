from django.db import models
from django.conf import settings
from Bank_database.models.Szamla import Szamla

class Tranzakcio(models.Model):
    szamla_id = models.ForeignKey(Szamla,on_delete=models.CASCADE)
    datatime = models.DateTimeField(auto_now_add=True , null=True, blank=True) #
    osszeg = models.FloatField()
    tranzakcio_fajta = models.CharField(max_length=255)
    activated = models.BooleanField(default = True)


    def __str__(self) -> str:
        return str(self.szamla_id)