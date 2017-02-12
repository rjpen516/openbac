from rest_framework import serializers
import datetime

class AuthSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=150)
