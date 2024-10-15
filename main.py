#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
import json
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData("N/A","N/A","N/A","N/A","N/A")


sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        city = row["city"]
        row["iataCode"] = flight_search.get_destination_codes(city=city)
        data_manager.update_destination_codes(row)
        time.sleep(2)
    flights = flight_search.check_flights(row)
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(cheapest_flight)
    


    
    





    

