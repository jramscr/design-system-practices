import time
import requests

while True:
    try:
        r = requests.get("http://server:5002/")
        print("Client got:", r.json())
    except Exception as e:
        print("Error:", e)
    time.sleep(2)   # every 2 seconds
