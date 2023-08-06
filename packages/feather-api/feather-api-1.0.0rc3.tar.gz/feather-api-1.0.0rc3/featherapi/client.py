import os

import requests

class DataClient:

    BASE_URL = 'https://dev.try-feather.com/v2'

    DEV_MODE = os.environ.get('FEATHER_API_DEV_MODE', None)

    if DEV_MODE:
        BASE_URL = 'https://dev.try-feather.com/v2'

    API_KEY = os.environ.get('FEATHER_API_KEY', None)

    def __init__(self, api_key=API_KEY):
        self.api_key = api_key

        session = requests.Session()
        session.headers.update({'x-api-key': api_key})

        self.session = session
    
    def get_equity_facts(self, symbol, start=None, end=None, section='all'):
        """ 
        Get all facts for a given equity symbol.
        
        Returns a dictionary of facts, grouped by what section of a financial report they belong to.

        The valid sections are:
        `key_financials`: Selected key financials and their growth rates year-over-year
        `income`: Company income statements
        `balance`: Company balance sheet
        `cashflow`: Company cashflow statement
        `ratios`: Calculated ratios based on financial report data
        `comp_fin`: View of comparable companies and their financials.
        `comp_mult`: View of comparable companys and their multiples.

        For the sections that represent financial statements, the facts are delivered, grouped, and listed as they appear on the statements.
        """
        path = f'/equity/{symbol}/facts/{section}'

        query_params = {}

        if start: query_params['start'] = start
        if end: query_params['end'] = end


        response = self.__get_url(path, query_params)
        data = response['data']
        return data

    def get_available_equity_facts(self, symbol):
        path = f'/equity/{symbol}/available'
        response = self.__get_url(path)
        data = response['data']
        return data
    
    def get_recent_stock_price(self, symbol, interval, limit=None):
        """
        Get the latest available stock prices for a given equity symbol.

        Parameters
        - `symbol`: The equity symbol to get the stock price for.
        - `interval`: The interval to get prices for. Valid values are `1m`, `5m`, `15m`, `30m`, `1h`, `4h`. For example, `1m` will return prices 1 minute apart
        - (Optional) `limit`: The number of values to return. Default is all available values.
        """

        if interval not in ['1m', '5m', '15m', '30m', '1h', '4h']:
            raise ValueError('Interval must be one of 1m, 5m, 15m, 30m, 1h, 4h')
        
        path = f'/equity/{symbol}/stock-price/{interval}'
        query_params = {}
        if limit: query_params['limit'] = int(limit)
        response = self.__get_url(path)
        data = response['data']
        return data
    
    def get_historical_stock_price(self, symbol, start, end):
        """
        Get the daily close prices for a given stock.

        Parameters
        - `symbol`: The equity symbol to get the stock price for.
        - `start`: The start date to get prices for. Format: `YYYY-MM-DD`
        - `end`: The end date to get prices for. Format: `YYYY-MM-DD`
        """

        if int(start.replace('-', '')) > int(end.replace('-', '')):
            raise ValueError('Start date must be before end date.')
        
        if start[5] != '-' or start[8] != '-':
            raise ValueError('Start date must be in the format YYYY-MM-DD')
        
        if end[5] != '-' or end[8] != '-':
            raise ValueError('End date must be in the format YYYY-MM-DD')
        
        path = f'/equity/{symbol}/stock-price-historical'
        query_params = {
            'start': start,
            'end': end
        }
        response = self.__get_url(path, query_params)
        data = response['data']
        return data

    def get_institutional_holders(self, symbol):
        path = f'/equity/{symbol}/institutional-holders'
        response = self.__get_url(path)
        data = response['data']
        return data
    
    def get_insider_trades(self, symbol):
        path = f'/equity/{symbol}/insider-trades'
        response = self.__get_url(path)
        data = response['data']
        return data

    def __get_url(self, path, query_params={}):
        url = self.BASE_URL + path

        session = self.session

        response = session.get(url, params=query_params)
        return response.json()
