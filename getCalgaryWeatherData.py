import requests
import os
import re

downloadUrl = 'https://calgary.weatherstats.ca/download.html'
formData = {
    'formdata': 'ok',
    'type': 'hourly',
    'limit': '50'
}

response = requests.post(downloadUrl, data=formData)
text = "\n".join(
    [line for line in response.text.split('\r\n') if line.strip() != ''])
text = text.replace('MDT', 'MST')

with open('calgaryWeather.csv', 'w+') as f:
    f.write(text)

print('Done')
