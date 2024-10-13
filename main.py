#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        city = row["city"]
        row["iataCode"] = flight_search.get_destination_codes(city=city)
        data_manager.update_destination_codes(row)
        




    

