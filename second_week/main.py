import requests
import json

data = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')

print(json.dumps(data.json()["dataseries"], indent=2))