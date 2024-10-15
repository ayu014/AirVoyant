import os
from twilio.rest import Client
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
api_key = os.environ.get("API_KEY")
from_n = '+18706003250'
to_n = '+916280059961'

class NotificationManager(Client):
    #This class is responsible for sending notifications with the deal flight details
    def __init__(self):
        self.client = Client(account_sid,auth_token)
        self.price = None
        self.origin = None
        self.destination = None
        self.out_date = None
        self.return_date = None
        self.message = None


    def send_msg(self,cheapest_flight_detail):
        if cheapest_flight_detail == None:
            return
        self.price = cheapest_flight_detail["price"]
        self.origin = cheapest_flight_detail["origin"]
        self.destination = cheapest_flight_detail["destination"]
        self.out_date = cheapest_flight_detail["out_date"]
        self.return_date = cheapest_flight_detail["return_date"]

        self.message = f"""Low Price Alert!\n Only {self.price} to fly from {self.origin} to {self.destination}, on {self.out_date[0]}, {self.out_date[1]} until {self.return_date[0]}, {self.return_date[1]}."""
        self.client.messages.create(
        body=self.message,
        from_=from_n,
        to=to_n
        )
    print("Sent the message")

        
        