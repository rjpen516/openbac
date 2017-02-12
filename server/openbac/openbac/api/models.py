from django.db import models

# Create your models here.
class UnregisteredDevice(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mac = models.CharField(max_length=50)


    def __str__(self):
        return str(self.mac)
