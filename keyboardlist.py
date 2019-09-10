import requests

r = requests.get('http://api.qmk.fm/v1/keyboards')
keyboards = r.json()