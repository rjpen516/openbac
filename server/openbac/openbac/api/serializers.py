from rest_framework import serializers
import datetime
from .models import UnregisteredDevice

class AuthSerializer(serializers.Serializer):
    card_id = serializers.CharField(max_length=150)


class ResponseSerializer(serializers.Serializer):
    auth_decision = serializers.BooleanField()
    led_color = serializers.CharField(max_length=50)


class ReaderBootstrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnregisteredDevice
        fields = ('id','username','password','mac')
