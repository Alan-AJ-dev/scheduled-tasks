import requests
from twilio.rest import Client

import os




MY_LAT = 11.981659
MY_LONG = 75.382952


parameters={
"lat":11.981685,
"lon":75.383226,
"cnt": 4,
"appid":api,
"formatted":0
}


# Initialize the Twilio client
client = Client(account_sid, auth_token)

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
data = requests.get(api_endpoint,params=parameters)
weather_data = data.json()
print(weather_data)
weather_id_lst = []
will_rain = False

for hour in weather_data["list"]:


    weather_id= int(hour["weather"][0]["id"])
    if weather_id < 700:
        will_rain = True
if will_rain:
    print("Bring Umberlla")
    # Send the message
    message = client.messages.create(
        body="Purath pokumbo kuda☂️ edukk kunne..!Mazha peyyum⛈️!",
        from_="+12544574675",  # Your Twilio phone number
        to="+919946890737"  # The recipient's phone number (with country code)
    )
    # Print the unique message SID to confirm it was sent
    print(f'Message sent successfully! Message SID: {message.sid}')


