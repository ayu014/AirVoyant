import os
import requests


TOEKN_EP = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
OFFERS_ENDPOINT = "https://test.api.amadeus.com/v1/shopping/flight-offers"



class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

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
        



    