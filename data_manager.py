import os
import requests
from requests.auth import HTTPBasicAuth


SHEET_GET_EP = "https://api.sheety.co/dbba13af5f31d6764ac91e103684a06a/flightDeals/prices"

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''
    def __init__(self):
        self._username = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._basic = HTTPBasicAuth(username= self._username,password=self._password)
        self.destination_data = {}

    def get_destination_data(self):
        with requests.get(url=SHEET_GET_EP,auth=self._basic) as response:
            response.raise_for_status()
            self.destination_data = response.json()["prices"]
            return self.destination_data
        
    def update_destination_codes(self,row):
        rowid = row["id"]
        Edit_EP = f"https://api.sheety.co/dbba13af5f31d6764ac91e103684a06a/flightDeals/prices/{rowid}"
        sheet_inputs = {
            "price" : {
                "iataCode" : row["iataCode"]
            }
        }
        with requests.put(url = Edit_EP,json = sheet_inputs,auth=self._basic) as sheet_response:
            sheet_response.raise_for_status()
            print("updated")
        
    

    

