import json

with open("church.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

geojson = {
    "type": "FeatureCollection",
    "features": []
}


features = []

for item in data:

    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                item['location']['lng'],
                item['location']['lat']
            ]
        },
        "properties": {
            "name": item['name']
        }
    })

geojson['features'] = features

with open("geojson.json", 'w', encoding='utf-8') as file:
    json.dump(geojson, file, ensure_ascii=False)
