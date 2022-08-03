from django.db import models

# Create your models here.

class Parametros(models.Model):
  gb = models.CharField(max_length=20, null=True, blank=True)
  mailTo = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return f'{self.gb}|{self.mailTo}'