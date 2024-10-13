import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

# SHEET_GET_EP = "https://api.sheety.co/dbba13af5f31d6764ac91e103684a06a/flightDeals/prices"

# username = os.environ.get("SHEETY_USERNAME")
# password = os.environ.get("SHEETY_PASSWORD")
# basic = HTTPBasicAuth(username= username,password=password)


# with requests.get(url=SHEET_GET_EP,auth=basic) as response:
#     response.raise_for_status()
#     destination_data = response.json()["prices"]
#     pprint(destination_data)
#     for data in destination_data:
#         rowid = data["id"]
#         Edit_EP = f"https://api.sheety.co/dbba13af5f31d6764ac91e103684a06a/flightDeals/prices/{rowid}"
#         sheet_inputs = {
#             "price" : {
#                 "city" : data["city"],
#                 "lowestPrice" : data["lowestPrice"],
#                 "iataCode" : "Testing"

#             }
#         }

#         with requests.put(url = Edit_EP,json = sheet_inputs,auth=basic) as sheet_response:
#             sheet_response.raise_for_status()
#             print("updated")

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
    response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=header,data=body)
    return response.json()["access_token"]



def get_destination_codes():
    token = get_new_token()
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    query = {
        "keyword" : "PARIS",
        "max" : "2",
        "include" :"AIRPORTS"

    }
    with requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",headers=headers,params=query) as response:
        code = response.json()["data"][0]["iataCode"]
        print(code)

get_destination_codes()







    
