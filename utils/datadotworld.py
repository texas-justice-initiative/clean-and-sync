import requests

BASE_URL = 'https://api.data.world/v0'


class Datadotworld:
    def __init__(self, settings, dataset):
        self.api_key = settings['api_key']
        self.dataset = dataset

    def sync(self):
        """
        Forces a dataset to synchronize all of it's sources.
        """
        url = f'{BASE_URL}/datasets/{self.dataset}/sync'
        headers = {'Authorization': f'Bearer {self.api_key}'}

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f'Failed to sync {self.dataset}')
            r.raise_for_status()
