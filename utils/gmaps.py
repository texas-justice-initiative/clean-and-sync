import requests

BASE_URL = 'https://maps.googleapis.com/maps/api'


class Gmaps:
    def __init__(self, settings):
        self.api_key = settings['api_key']

    def geocode(self, address):
        url = f'{BASE_URL}/geocode/json'

        params = {
            'address': address,
            'key': self.api_key,
        }

        r = requests.get(url, params=params)
        if r.status_code != 200:
            print(f'Failed to geocode {address}')
            r.raise_for_status()

        lat = lng = ''
        try:
            coordinates = r.json()['results'][0]['geometry']['location']
            lat, lng = coordinates['lat'], coordinates['lng']
        except Exception:
            pass

        return lat, lng
