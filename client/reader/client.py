#!/usr/bin/python

import argparse
import pprint
import sys
import requests
import json


parser = argparse.ArgumentParser(description='OpenBAC Reader Client')
parser.add_argument('--config', metavar='-c', type=str, nargs='?',
                    help='Config Path on the filesystem (defaults to /opt/openbac/config.ini)',
                    default='/opt/openbac/config.ini')

parser.add_argument('--input', metavar='-i', type=str, nargs='?',
                    help='Input source of the external reader (defaults to stdin)',
                    default='stdin')
parser.add_argument('--server', metavar='-s', type=str, nargs='?',
                    help='The remote server to send events to',
                    default='localhost')

parser.add_argument('--username', metavar='-u', type=str, nargs='?',
                    help='Username to log into remote server',
                    default='username')

parser.add_argument('--password', metavar='-p', type=str, nargs='?',
                    help='Password to log into remote server',
                    default='password')


args = parser.parse_args()

pprint.pprint(args)


print("Starting reader loop")


def input():
    if args.input == 'stdin':
        print "Enter Card: "
        data = sys.stdin.readline().replace('\n','')
        return data


SERVER = args.server
LOGIN_URL = '/api/api-token-auth/'
CARD_AUTH = '/api/cardauthrequest/'

while True:



    #wait for some Input
    card_id = input()

    #login to the server
    s = requests.Session()

    response = s.post(SERVER + LOGIN_URL, data={'username': args.username, 'password': args.password})
    token = json.loads(response.text)['token']
    s.headers.update({'Authorization': "JWT " + token})

    #make a get request to the server, preparing for request
    response = s.get(SERVER + CARD_AUTH)
    #make request to server with card data
    response = s.post(SERVER + CARD_AUTH, data={'card_id': card_id, 'piv_token_signed': ''})
    #display output to the user
    print response.text
