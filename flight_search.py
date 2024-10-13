import os
import requests
from datetime import datetime, timedelta


TOEKN_EP = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"



class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()


        self.now = datetime.now()
        self.tomorrow_date = self.now + timedelta(days=1)
        self.tomorrow_date_str = self.tomorrow_date.strftime("%Y-%m-%d")
        self.return_date = self.tomorrow_date + timedelta(days=180)
        self.return_date_str = self.return_date.strftime("%Y-%m-%d")

    def _get_new_token(self):
        header = {
            "content-type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret
        }
        response = requests.post(url=TOEKN_EP,headers=header,data=body)
        return response.json()["access_token"]
        
    
    
    def get_destination_codes(self,city):
        headers = {
            "Authorization" : f"Bearer {self._token}"
        }
        query = {
            "keyword" : city,
            "max" : "2",
            "include" :"AIRPORTS"

        }
        with requests.get(url=IATA_ENDPOINT,headers=headers,params=query) as response:
            try:
                code = response.json()["data"][0]["iataCode"]
            except IndexError:
                print(f"Index Error : No airport code found for {city}")
                return "N/A"
            except KeyError:
                print(f"Index Error : No airport code found for {city}")
                return "N/A"
            return code
        
    def check_flights(self,row):
        headers = {
            "Authorization" : f"Bearer {self._token}"
        }
        query = {
            "originLocationCode" : "LON",
            "destinationLocationCode" : row["iataCode"],
            "departureDate" : self.tomorrow_date_str,
            "returnDate" : self.return_date_str,
            "adults" : 1,
            "nonStop" : "true",
            "currencyCode" : "GBP",
            "max" : 10
        }
        with requests.get(url=FLIGHT_ENDPOINT,headers=headers,params=query) as response:
            if response.status_code != 200:
                print(f"Check Flights : Response Code : {response.status_code}")
                print("There was a problem with flight search.\nFor details on status code check documentation.")
                print(response.text)
                return None
            return response.json()
        




    



    