import requests
from datetime import datetime


MY_LAT = 12.908860
MY_LONG = 77.599055

iss_latitude = 12.908860-5
iss_longitude = 73.000000

def is_iss_near_me():
    if MY_LONG - iss_longitude in range(float(MY_LONG-5,MY_LONG+ 5)) and MY_LAT - iss_latitude in range(float(MY_LAT-5, MY_LONG+5)):
        print("Near me")
    else:
        print("Not near me")

is_iss_near_me()
