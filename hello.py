import requests
response = requests.get('https://api.github.com')
print(response.status_code)
latitude= 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
response=requests.get(url)
data = response.json()

print(data)


#status last checked on 2024-06-01=200
#status last checked on 2024-06-01= {'latitude': 48.84, 'longitude': 2.3599997, 'generationtime_ms': 0.001430511474609375, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 46.0
# 2:58:46 yt vid

