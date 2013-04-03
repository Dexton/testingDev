from django.db import models
from spurningar.models import Spurning

class Svar(models.Model):
    numer = models.IntegerField(default=1)
    texti = models.CharField(max_length=9999)
    rettEdaRangt = models.BooleanField(default=False)
    spurning = models.ForeignKey(Spurning)

class Comment(models.Model):
    maelandi = models.CharField(maxlength=200)
    texti = models.CharField(maxlength=500)
    svar = models.ForeignKey(Svar)
