from rest_framework import serializers
import datetime
from .models import UnregisteredDevice

class AuthSerializer(serializers.Serializer):
    card_id = serializers.CharField(max_length=150)
    piv_token_signed = serializers.CharField(max_length=300, allow_blank=True)


class ResponseSerializer(serializers.Serializer):
    auth_decision = serializers.BooleanField()
    led_color = serializers.CharField(max_length=50)


class ReaderBootstrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnregisteredDevice
        fields = ('id','username','password','mac')


class RelayAckSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=200)


class RelayResponse(serializers.Serializer):
    seconds_open = serializers.IntegerField(min_value=0, max_value=500)
    unlock = serializers.BooleanField()
