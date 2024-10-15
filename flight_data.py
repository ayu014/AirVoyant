class FlightData:
    def __init__(self):
        self.price = None
        self.origin_airport = None
        self.destination_airport = None
        self.out_date = None
        self.return_date = None

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


                







    