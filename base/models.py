from django.db import models

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=80)
    desc = models.CharField(max_length=200, null=True, blank=True)
