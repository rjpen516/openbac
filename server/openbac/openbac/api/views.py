from django.shortcuts import render

import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthSerializer, ResponseSerializer

from openbac.bac.models import Event, Relay, Action, Cardholder

# Create your views here.

class Auth_request(APIView):

    serializer_class = AuthSerializer
    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        print serializer
        if serializer.is_valid():

            parsed_data = serializer.data
            card_id = parsed_data['card_id']

            try:
                cardholder = Cardholder.objects.get(card_id=card_id)
            except Cardholder.DoesNotExist:
                cardholder = None

            event = Event()
            event.time = datetime.datetime.now()
            event.reader = request.user.reader
            event.relay = Relay.objects.get(paired_reader=request.user.reader.id)
            if cardholder:

                event.cardholder = cardholder
                event.action_taken = event.relay.action
                event.save()
                return_data = ResponseSerializer(data={'auth_decision': True, 'led_color': "green"})
            else:
                event.action_taken = event.relay.action
                event.save()
                return_data = ResponseSerializer(data={'auth_decision': False, 'led_color': "red"})



            #add logic code, check if card is allowed, send request to relay


            return_data.is_valid()
            return Response(return_data.data, status=status.HTTP_202_ACCEPTED)
