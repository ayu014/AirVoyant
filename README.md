# AirVoyant - Flight Deal Finder

AirVoyant is a Python-based application that helps you find the best and cheapest flight deals over the next 180 days. It searches for flights from a specific origin to various destinations, compares prices, and notifies you via text message when the flight details are the cheapest available.

## Features
- Fetches flight data from the Amadeus Flight API.
- Finds the cheapest available flight based on destination, departure, and return dates.
- Compares multiple flights and logs the best price.
- Sends an email notification when a flight with the lowest price is found.
- Automatically searches for deals 180 days into the future.

## How It Works
1. **Flight Data**: Retrieves flight offers from the Amadeus Flight API.
2. **Price Comparison**: Finds the cheapest available flight by comparing prices for different dates and destinations.
3. **Notifications**: Once the lowest fare is found, an email notification is sent.
   
The program checks flights from a defined origin to various destinations, retrieves the IATA codes for each destination, and finds the best deals by checking daily prices. 

## Setup and Installation
To get started, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/flight-deal-finder.git
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    source venv/bin/activate  # Linux/Mac
    .venv\Scripts\Activate.ps1  # Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables**:
    You will need an API key and secret from [Amadeus API](https://developers.amadeus.com/) and [Twilio API](https://www.twilio.com/en-us). Add these environment variables:
    ```
    AMADEUS_API_KEY = <your_api_key>
    AMADEUS_API_SECRET = <your_api_secret>
    TWILIO_ACCOUNT_SID = <your_unique_sid>
    TWILIO_AUTH_TOKEN = <your_unique_token>
    TWILIO_API_KEY = <your_api_key>
    TWILIO_MOBILE_NUMBER = <your_twilio_generated_number>
    TO_MOBILE_NUMBER = <your_personal_number>
    ```
5. **Run the Program**:  Start the program by running:  
    ```bash
    python main.py
    ```


## APIs Used
- [Amadeus Flight API](https://developers.amadeus.com/) for fetching flight data.
- [Twilio API](https://www.twilio.com/en-us) for sending personalized text messages.

## Notifications
Text messages are sent using a notification manager that sends alerts for the cheapest flights. The mobile number credentials can be configured using the environment variables.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

