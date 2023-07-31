import json
import time
import requests
from geogather.googlemaps.map import generate_search_url, get_extra_data, scrape_google_map,extract_info_from_response
from geogather.utils.generate import gen_search_points_from_square
from geogather.utils.filter import filter_bad_data

center = (27.700629106875546, 85.32850170695393)
query = "church"
distance = 100
points = 7
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

urls = gen_search_points_from_square(
    center_coordinate=center, distance=distance, points=points)

data = []

for index, item in enumerate(urls):
    q = generate_search_url(item, postal_code=None, query=query, center=center)
    print(index)
    try:
        res = requests.get(f"http://127.0.0.1:5000/process?q={q}", timeout=60)
        res = res.json()
        url = res['data']['url']
        if not url:
            continue
        data.append(extract_info_from_response(res['data']['response']))
        new_data = get_extra_data(url, agent)

        data.extend(new_data)
    except Exception as e:
        print(e)

dat = scrape_google_map(data)


d = filter_bad_data(dat,center=center,radius=distance)

print(len(d))

with open("c.json", 'w', encoding='utf-8') as file:
    json.dump(d, file)