from django.db import models

# Create your models here.

class Esame(models.Model):
    id              = models.AutoField      (primary_key=True),
    paziente        = models.ForeignKey     ('Paziente', on_delete=models.CASCADE)
    data_ora        = models.DateTimeField  (null=True),
    valore          = models.FloatField     (null=True),
    unita_misura    = models.CharField      (null=True, max_length=20),


class Paziente(models.Model):
    fiscalCode  = models.CharField  (primary_key=True, max_length=16),
    name        = models.CharField  (max_length=255),
    surname     = models.CharField  (max_length=255),
