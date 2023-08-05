import os

import requests

class DataClient:

    BASE_URL = 'https://api.try-feather.com/v2'

    API_KEY = os.environ.get('FEATHER_API_KEY', None)

    def __init__(self, api_key=API_KEY):
        self.api_key = api_key

        session = requests.Session()
        session.headers.update({'x-api-key': api_key})

        self.session = session
    
    def get_equity_facts(self, symbol, start=None, end=None):
        path = f'/equity/facts/{symbol}/all'

        query_params = {}

        if start: query_params['start'] = start
        if end: query_params['end'] = end


        response = self.__get_url(path, query_params)
        data = response['data']
        return data

    def get_available_equity_facts(self, symbol):
        path = f'/equity/facts/{symbol}/available'
        response = self.__get_url(path)
        data = response['data']
        return data

    def __get_url(self, path, query_params={}):
        url = self.BASE_URL + path

        session = self.session

        response = session.get(url, params=query_params)
        return response.json()
