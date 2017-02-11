from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.TextField()
    longitude = models.DecimalField(decimal_places=8, max_digits=14)
    latitude = models.DecimalField(decimal_places=8, max_digits=14)

class Action(models.Model):
    name = models.TextField()
    open_relay = models.BooleanField()
    open_time = models.IntegerField()


class Reader(models.Model):
    name = models.TextField()
    location =models.ForeignKey(Location)
    ipaddr = models.TextField()
    install_date = models.TextField()

class Relay(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    ipaddr = models.TextField()
    install_date = models.TextField()
    paired_reader = models.ForeignKey(Reader)


class Access_group(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    reader = models.ForeignKey(Reader)
    action = models.ForeignKey(Action)


class Event(models.Model):
    time = models.DateTimeField()
    reader = models.ForeignKey(Reader)
    relay = models.ForeignKey(Relay)
    action_taken = models.ForeignKey(Action)
