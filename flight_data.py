# class FlightData:
#     #This class is responsible for structuring the flight data.
#     def __init__(self,price,origin_airport,destination_airport,out_date,return_date):
#         self.price = price
#         self.origin_airport = origin_airport
#         self.destination_airport = destination_airport
#         self.out_date = out_date
#         self.return_date = return_date
        

#     def find_cheapest_flight(self,data):
#         if self.data is None or not self.data["data"]:
#             print("No Flight Data")
#             return FlightData("N/A","N/A","N/A","N/A","N/A")
        
#         self.first_flight = self.data["data"][0]
#         self.lowest_price = float(self.first_flight["price"]["grandTotal"])
#         self.origin = self.first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
#         self.destination = self.first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
#         self.out_date = self.first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
#         return_date = self.first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

#          # Initialize FlightData with the first flight for comparison
#         cheapest_flight = FlightData(self.lowest_price, self.origin, self.destination, self.out_date, self.return_date)

#         for flight in data["data"]:
#             self.price = float(flight["price"]["grandTotal"])
#             if self.price < self.lowest_price:
#                 self.lowest_price = self.price
#                 self.origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
#                 self.destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
#                 self.out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
#                 self.return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
#                 self.cheapest_flight = FlightData(self.lowest_price, self.origin, self.destination, self.out_date, self.return_date)
#                 print(f"Lowest price to {self.destination} is £{self.lowest_price}")

#         return self.cheapest_flight


class FlightData:
    def __init__(self,price,origin_airport,destination_airport,out_date,return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(self,all_flights):
        if all_flights is None or not all_flights["data"]:
            return None
        
        #Initialze the first flight_data for comparisons:
        self.lowest_price = all_flights["data"][0]["price"]["grandTotal"]
        self.origin_airport = all_flights["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        self.destination_airport = all_flights["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        self.out_date = all_flights["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")
        self.return_date = all_flights["data"][0]["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")

        result = all_flights["data"]
        for data in result:
            temp_price = data["price"]["grandTotal"]
            if temp_price < self.lowest_price:
                self.lowest_price = temp_price
                self.origin_airport = data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                self.destination_airport = data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                self.out_date = data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")
                self.return_date = data["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")
            self.price = self.lowest_price

        cheapest_flight_data = {
            "price" : self.price,
            "origin" : self.origin_airport,
            "destination" : self.destination_airport,
            "out_date" : self.out_date,
            "return_date" : self.return_date
        }

        return cheapest_flight_data


                







    