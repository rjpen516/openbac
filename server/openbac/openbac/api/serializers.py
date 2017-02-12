from rest_framework import serializers
import datetime

class AuthSerializer(serializers.Serializer):
    card_id = serializers.CharField(max_length=150)


class ResponseSerializer(serializers.Serializer):
    auth_decision = serializers.BooleanField()
    led_color = serializers.CharField(max_length=50)
