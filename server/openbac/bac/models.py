from django.db import models

# Create your models here.

class reader(models.Model):
    name = models.StringField()
    location =models.ForeignKey(location)
    ipaddr = models.StringField()
    install_date = models.StringField()

class relay(models.Model):
    name = models.StringField()
    location = models.ForeignKey(location)
    ipaddr = models.StringField()
    install_date = models.StringField()
    paired_reader = models.ForeignKey(reader,on_delete=models.CASCADE)


class access_group(models.Model):
    name = models.StringField()
    location = models.ForeignKey(location)
    reader = models.ForeignKey(reader)
    action = models.ForeignKey(action)


class event(models.Model):
    time = models.DateTimeField()
    reader = models.ForeignKey(reader)
    relay = models.ForeignKey(relay)
    action_taken = models.ForenKey(action)


class location(models.Model):
    name = models.StringField()
    longitude = models.DecimalField()
    latitude = models.DecimalField()


class action(models.Model):
    name = models.StringField()
    open_relay = model.BooleanFiled()
    open_time = model.IntegerFiled()
