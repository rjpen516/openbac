from django.db import models

# Create your models here.

class Reader(models.Model):
    name = models.StringField()
    location =models.ForeignKey(location)
    ipaddr = models.StringField()
    install_date = models.StringField()

class Relay(models.Model):
    name = models.StringField()
    location = models.ForeignKey(location)
    ipaddr = models.StringField()
    install_date = models.StringField()
    paired_reader = models.ForeignKey(reader,on_delete=models.CASCADE)


class Access_group(models.Model):
    name = models.StringField()
    location = models.ForeignKey(location)
    reader = models.ForeignKey(reader)
    action = models.ForeignKey(action)


class Event(models.Model):
    time = models.DateTimeField()
    reader = models.ForeignKey(reader)
    relay = models.ForeignKey(relay)
    action_taken = models.ForenKey(action)


class Location(models.Model):
    name = models.StringField()
    longitude = models.DecimalField()
    latitude = models.DecimalField()


class Action(models.Model):
    name = models.StringField()
    open_relay = model.BooleanFiled()
    open_time = model.IntegerFiled()
