from django.db import models
from fag.models import Faghluti


class Hraefni(models.Model):
    texti = models.CharField(max_length = 9999)

class Mynd(models.Model):
    mynd = models.ImageField(upload_to='images/')
    rodun = models.IntegerField(default=0)
    texti = models.CharField(max_length = 200)
    spurning = models.ForeignKey(Spurning)

class Spurning(models.Model):
    argangur = models.IntegerField(default=1)
    erfidleiki = models.FloatField()
    textahluti = models.CharField(max_length=1000)
    faghluti = models.ForeignKey(Faghluti)
    hraefni = models.ForeignKey(Hraefni)
