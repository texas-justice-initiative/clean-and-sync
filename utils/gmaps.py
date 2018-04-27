import requests

BASE_URL = 'https://maps.googleapis.com/maps/api'


class Gmaps:
    def __init__(self, settings):
        self.api_key = settings['api_key']

    def geocode(self, address):
        """
        Finds the latitude and longitude coordinates of an address.

        :param str address: A postal-style address, e.g. 123 Main St, Austin, TX 78758
        :return: Latitude and longitude coordinates
        :rtype: str, str
        """
        url = f'{BASE_URL}/geocode/json'

        params = {
            'address': address,
            'key': self.api_key,
        }

        r = requests.get(url, params=params)
        if r.status_code != 200:
            print(f'Failed to geocode {address}')
            r.raise_for_status()

        lat = lng = None
        try:
            coordinates = r.json()['results'][0]['geometry']['location']
            lat, lng = coordinates['lat'], coordinates['lng']
        except Exception:
            pass

        return lat, lng
