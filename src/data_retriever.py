from abc import ABC
import os
from dotenv import load_dotenv
import requests
import openfeed
import logging

from Exceptions.api_exceptions import StockAPIConnectionError


logger = logging.getLogger(__name__)

class DataRetriever(ABC):


    def retrieve_data(self, data) -> any:
        pass



class DataRetrieverImpl(DataRetriever):

    def __init__(self):
        self.username_api = os.getenv('BARCHART_USERNAME')
        self.password_api = os.getenv('BARCHART_PASSWORD')
        assert self.username_api is not None, 'BARCHART_USERNAME is not set'
        assert self.password_api is not None, 'BARCHART_PASSWORD is not set'

    
    def build_url(self,etf_ticker:str):
        assert isinstance(etf_ticker, str)
        return f"https://openfeed.aws.barchart.com/stream/quote.jsx?symbols={etf_ticker}&username={self.username_api}&password={self.password_api}&version=json"
    
    def retrieve_data(self, data:str) -> any:
        r = requests.get(self.build_url(data))
        data = r.json()
        print(data)

    
class DataRetrieverMock(DataRetriever):

    def retrieve_data(self, data:str) -> any:
        return data

