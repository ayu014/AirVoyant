#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification = NotificationManager()


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
    notification.send_msg(cheapest_flight_detail=cheapest_flight)
    break
    
    


    
    





    

