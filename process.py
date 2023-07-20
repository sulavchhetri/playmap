import requests

q = "https://www.google.com/maps/search/cafes+in+new+york/@40.7380004,-74.011112,14z/data=!4m2!2m1!6e5?hl=en"

url = f"http://172.104.39.169:5000/process?q={q}"

res = requests.get(url)

print(res.text)