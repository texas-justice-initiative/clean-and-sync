import requests

BASE_URL = 'https://geocoding.geo.census.gov/geocoder'


class Census:

    @staticmethod
    def reverse_geocode(lat, lng):
        """
        Given latitude and longitude coordinates, will return the affiliated census tract.

        :param str lat: Latitude coordinate
        :param str lng: Longitude coordinate
        :return: Comma-separated list of found census tracts -- should be one entry, though
        :rtype: str
        """
        url = f'{BASE_URL}/geographies/coordinates'

        params = {
            'benchmark': 'Public_AR_Census2010',
            'vintage': 'Census2010_Census2010',
            'layers': 'Census Tracts',
            'x': lng,
            'y': lat,
            'format': 'json',
        }

        r = requests.get(url, params=params)
        if r.status_code != 200:
            print(f'Failed to reverse geocode (lat: {lat}, lng: {lng})')
            r.raise_for_status()

        tracts = None
        try:
            raw_tracts_data = r.json()['result']['geographies']['Census Tracts']
            tracts = ','.join((t['TRACT'] for t in raw_tracts_data))
        except Exception:
            pass

        return tracts
