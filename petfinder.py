import requests
import os
from pprint import pformat
from flask import request
import json

#note: . secrets.sh everytime you open the terminal

API_KEY = os.environ['PETFINDER_KEY']
SECRET_KEY = os.environ['PETFINDER_SECRET']

def get_token():
    """Returns authorization token from petfinder"""
    
    url = "https://api.petfinder.com/v2/oauth2/token"
    data = {
      'grant_type': 'client_credentials',
      'client_id': API_KEY,
      'client_secret': SECRET_KEY
    }
    response = requests.post(url, data=data)
    res = response.json()
    token = res['token_type'] + ' ' + res['access_token']

    return token


def search_petfinder():
    """Return API response based on user search input - get animals endpoint"""

    token = get_token()
    url = "https://api.petfinder.com/v2/animals"
    headers = {'Authorization': token}
    location_search = request.args.get('search', '')
    miles = int(request.args.get('miles', ''))
    payload = {'type': 'Cat',
               'limit':5,
               'location': location_search,
               'distance': miles,
               'size': 'xlarge,large'}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json() #python dictionary
    return data




#data from get_animals endpoint:
#SHELTERS Table
#organization_id = data['animals'][0]['organization_id']





# demo show SF, if SF location is chosen then get images from the database and not the API
##select random images but keep track of what's being pulled

#use animal id (in the API) to store cats to favorites. 
##this will be the foregin key in the favorites tables which is the primary key of the cats table

#you can use sessions to check if someone is logged in (example)


#data - dict
#data[animals] - type is list - list of all the animals in the response
#data[animals][0] - type is dict - dict of all the details of the animal at index 0
