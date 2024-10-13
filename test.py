import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta




########################################################################################
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
def get_new_token():
    api_key = os.environ.get("AMADEUS_API_KEY")
    api_secret = os.environ.get("AMADEUS_API_SECRET")
    header = {
            "content-type": "application/x-www-form-urlencoded"
        }
    body = {
        "grant_type" : "client_credentials",
        "client_id" : api_key,
        "client_secret" : api_secret
    }
    with  requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=header,data=body) as response:
        return response.json()["access_token"]


def check_flights():
    token = get_new_token()
    now = datetime.now()
    tomorrow_date = now + timedelta(days=1)
    tomorrow_date_str = tomorrow_date.strftime("%Y-%m-%d")
    return_date = tomorrow_date + timedelta(days=180)
    return_date_str = return_date.strftime("%Y-%m-%d")

    headersx = {
        "Authorization" : f"Bearer {token}"
    }
    query = {
        "originLocationCode" : "LON",
        "destinationLocationCode" : "PAR",
        "departureDate" : tomorrow_date_str,
        "returnDate" : return_date_str,
        "adults" : 1,
        "nonStop" : "true",
        "currencyCode" : "GBP",
        "max" : 10
    }

    with requests.get(url=FLIGHT_ENDPOINT,headers=headersx,params=query) as response:
        response.status_code
        print()
        print(response.text)



check_flights()











    
