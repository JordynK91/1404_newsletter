import requests
from constants import URL_USA, URL_DC, URL_MD, URL_VA

class CovidAPI(object):

    def __init__(self):
        pass

    def get_usa_data(self):
        data_dict = self._get_data(URL_USA)
        data_dict.update(region='United States of America')
        return data_dict
        
    def get_md_data(self):
        data_dict = self._get_data(URL_MD)
        data_dict.update(region='Maryland')
        return data_dict
        
    def get_va_data(self):
        data_dict = self._get_data(URL_VA)
        data_dict.update(region='Virginia')
        return data_dict

    def get_dc_data(self):
        data_dict = self._get_data(URL_USA)
        data_dict.update(region='Washington, DC')
        return data_dict

    def _get_data(self, url):
        response = requests.get(url)
        if url == URL_USA:
            json_response = response.json()[0]
        else:
            json_response = response.json()
        parsed_dict = self._data_parsing(json_response)
        return parsed_dict

    def _data_parsing(self, response):
        positive = response.get('positive')
        positive_increase = response.get('positiveIncrease')
        death = response.get('death')
        death_increase = response.get('deathIncrease')
        covid_dict = {
                'positive': positive, 
                'positive_increase': positive_increase, 
                'death': death,
                'death_increase': death_increase
            }
        return covid_dict