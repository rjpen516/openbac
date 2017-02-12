from django.shortcuts import render

import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthSerializer

from openbac.bac.models import Event

# Create your views here.

class Auth_request(APIView):

    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)

        if serializer.is_valid():
            event = Event()
            event.time = datetime.datetime.now()
            event.reader = request.user.get_profile().reader
            event.relay = request.user.get_profile().reader.relay
            event.action_taken = 1
            event.save()

            #add logic code, check if card is allowed, send request to relay

            return Response(serializer.data, status=status.HTTP_200)
