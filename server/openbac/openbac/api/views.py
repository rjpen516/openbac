from django.shortcuts import render

import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthSerializer, ResponseSerializer

from openbac.bac.models import Event, Relay, Action

# Create your views here.

class Auth_request(APIView):

    serializer_class = AuthSerializer
    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)

        if serializer.is_valid():
            event = Event()
            event.time = datetime.datetime.now()
            event.reader = request.user.reader
            event.relay = Relay.objects.get(paired_reader=request.user.reader.id)


            event.action_taken = event.relay.action
            event.save()

            #add logic code, check if card is allowed, send request to relay

            return_data = ResponseSerializer(data={'auth_decision': True, 'led_color': "green"})
            return_data.is_valid()
            return Response(return_data.data, status=status.HTTP_202_ACCEPTED)
