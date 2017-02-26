from django.db import models

# Create your models here.
from enum import Enum
from django.utils.crypto import get_random_string
import datetime

class CardTypeEnum(Enum):
    PIV_CARD = 1
    PROX_PRO = 2



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
    mac = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name + " - " + str(self.location)

class Relay(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    ipaddr = models.TextField(blank=True)
    install_date = models.TextField(blank=True)
    action = models.ForeignKey(Action)
    paired_reader = models.ForeignKey(Reader, blank=True)
    mac = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name + " relay is attacked to " + str(self.paired_reader.name) + " @ " + str(self.location)


class Access_group(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    reader = models.ForeignKey(Reader)
    action = models.ForeignKey(Action)

class Cardholder(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.TextField(max_length=50)
    card_id = models.TextField()
    card_id_type = models.IntegerField()
    locations_allowed = models.ManyToManyField(Location)

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.card_id


class Event(models.Model):
    time = models.DateTimeField()
    reader = models.ForeignKey(Reader)
    relay = models.ForeignKey(Relay)
    action_taken = models.ForeignKey(Action)
    card_holder = models.ForeignKey(Cardholder, null=True, blank=True)
    token = models.CharField(max_length=200)
    expired = models.BooleanField(default=False)

    def create_transation(self, cardholder, action, reader, relay):
        self.card_holder = cardholder
        self.action_taken = action
        self.token = get_random_string(length=32)
        self.reader = reader
        self.relay = relay
        self.time = datetime.datetime.now()
        self.save()
        return self.token


    def __str__(self):
        return str(self.card_holder) + " accessed " + str(self.reader) + " at " + str(self.time)
