from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.TextField()
    longitude = models.DecimalField(decimal_places=8, max_digits=14)
    latitude = models.DecimalField(decimal_places=8, max_digits=14)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.TextField()
    open_relay = models.BooleanField()
    open_time = models.IntegerField()

    def __str__(self):
        return self.name + " open for " + str(self.open_time) + " secs"


class Reader(models.Model):
    name = models.TextField()
    location =models.ForeignKey(Location)
    ipaddr = models.TextField(blank=True)
    install_date = models.TextField(blank=True)

    def __str__(self):
        return self.name + " - " + str(self.location)

class Relay(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    ipaddr = models.TextField(blank=True)
    install_date = models.TextField(blank=True)
    action = models.ForeignKey(Action)
    paired_reader = models.ForeignKey(Reader)

    def __str__(self):
        return self.name + " relay is attacked to " + str(self.paired_reader.name) + " @ " + str(self.location)


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