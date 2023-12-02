from django.db import models

# Create your models here.
class Ram(models.Model):
    avaliable_ram = models.IntegerField()
    date = models.CharField(max_length=30)
