from django.db import models

#Fag

class Fag(models.Model):
    name = models.CharField(max_length=200)
    minArgangur = models.IntegerField(default=0)
    maxArgangur = models.IntegerField(default=0)

class Faghluti(models.Model):
    hluti = models.CharField(max_length=200)
    fag = models.ForeignKey(Fag)
