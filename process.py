import requests
import time
from geogather.googlemaps.map import extract_info_from_response

map_urls = [
    "https://www.google.com/maps/search/cafes+in+los+angeles/@34.052235,-118.243683,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in+london/@51.507351,-0.127758,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in+tokyo/@35.6895,139.6917,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in+sydney/@-33.8688,151.2093,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in+paris/@48.8566,2.3522,12z?hl=en",
    "https://www.google.com/maps/search/cafes+in/new+york/@40.7380004,-74.011112,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in/san+francisco/@37.774929,-122.419418,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in/berlin/@52.5200,13.4050,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in/toronto/@43.651070,-79.347015,19z?hl=en",
    "https://www.google.com/maps/search/cafes+in/amsterdam/@52.3680,4.9036,19z?hl=en"
]

initial = time.time()

for q in map_urls:
    url = f"http://172.104.39.169:5000/process?q={q}"


    res = requests.get(url)
    response = res.json()
    if not response.get("data",{}).get("url",None):
        print("No url")
        continue

    if data := response['data']['response']:
        parsed_data = extract_info_from_response(data)
        if parsed_data:
            print("Done")
        else:
            print("Bad data")
    else:
        print("Absent data")

total = time.time()- initial

print(int(total/10))