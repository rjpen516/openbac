from django.shortcuts import render

import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics

from .serializers import AuthSerializer, ResponseSerializer, ReaderBootstrapSerializer, RelayAckSerializer, RelayResponse
from .permissions import IsSuperUserFullOrAnyonePost
from .models import UnregisteredDevice

from openbac.bac.models import Event, Relay, Action, Cardholder

from django.utils.crypto import get_random_string

import pika

# Create your views here.

class Auth_request(APIView):

    serializer_class = AuthSerializer

    def get(self,request,format=None):
        return Response(data={'piv_token': get_random_string(32)})

    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        print serializer
        if serializer.is_valid():

            parsed_data = serializer.data
            card_id = parsed_data['card_id']

            if parsed_data['piv_token_signed']: #TODO - check to see if the reader is PIV enabled, if so we should force PIV for the transation.
                print "We got a PIV card, use public key to verify rather than card id"

            try:
                cardholder = Cardholder.objects.get(card_id=card_id)
            except Cardholder.DoesNotExist:
                cardholder = None

            event = Event()
            event.time = datetime.datetime.now()
            event.reader = request.user.reader
            event.relay = Relay.objects.get(paired_reader=request.user.reader.id)
            if cardholder:

                token = event.create_transation(cardholder,event.relay.action, request.user.reader, Relay.objects.get(paired_reader=request.user.reader.id))

                #call rabitmq to notify our relay with the token
                print("Notifing %s with token %s"%(event.relay, token))

                connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
                channel = connection.channel()
                rabbitmq_relay_queue = 'relay-' + str(Relay.objects.get(paired_reader=request.user.reader.id).id)
                channel.queue_declare(queue=rabbitmq_relay_queue)
                channel.basic_publish(exchange='',
                      routing_key=rabbitmq_relay_queue,
                      body=token)
                connection.close()


                return_data = ResponseSerializer(data={'auth_decision': True, 'led_color': "green"})
            else:
                event.action_taken = event.relay.action
                event.save()
                return_data = ResponseSerializer(data={'auth_decision': False, 'led_color': "red"})



            #add logic code, check if card is allowed, send request to relay


            return_data.is_valid()
            return Response(return_data.data, status=status.HTTP_202_ACCEPTED)
        return Response('', status=status.HTTP_400_BAD_REQUEST)


class Relay_ack(APIView):
    serializer_class = RelayAckSerializer
    def post(self, request, format=None):
        serializer = RelayAckSerializer(data=request.data)
        if serializer.is_valid():
            parsed_data = serializer.data

            #lets look up an event token, see if it is valid, and not to far from our requeset time
            event = Event.objects.get(token=parsed_data['token'])
            #print  str(event.relay.id) + " " + str(request.user.id)
            if event and event.relay.id == request.user.id and event.expired == False:  #TODO add timechecking
                event.expired = True
                event.save()
                return_data = RelayResponse(data={'seconds_open': event.action_taken.open_time, 'unlock': True})
            else:
                return_data = RelayResponse(data={'seconds_open': 0, 'unlock': False})

            return_data.is_valid()
            return Response(return_data.data, status=status.HTTP_202_ACCEPTED)


class ReaderBootstrap(generics.CreateAPIView):
    queryset = UnregisteredDevice.objects.all()
    serializer_class = ReaderBootstrapSerializer
    permission_classes = (IsSuperUserFullOrAnyonePost,)
