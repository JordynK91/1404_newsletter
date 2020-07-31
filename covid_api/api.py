import requests

URL_USA = 'https://covidtracking.com/api/v1/us/current.json'
URL_MD = 'https://covidtracking.com/api/v1/states/md/current.json'
URL_DC = 'https://covidtracking.com/api/v1/states/dc/current.json'
URL_VA = 'https://covidtracking.com/api/v1/states/va/current.json'

class CovidAPI(object):

    def __init__(self):
        pass

    def get_usa_data(self):
        return self.get_data(URL_USA)
        
    def get_md_data(self):
        return self.get_data(URL_MD)
        
    def get_va_data(self):
        return self.get_data(URL_VA)

    def get_dc_data(self):
        return self.get_data(URL_DC)

    def _get_data(self, url):
        response = requests.get(url_usa)
        parsed_dict = self._data_parsing(response)

    def _data_parsing(self, response):
        positive = response.get('positive')
        positive_increase = response.get('positiveIncrease')
        death = response.get('death')
        death_increase = response.get('deathIncrease')
        covid_dict = {
                'positive': positive, 
                'positive_increase' positive_increase, 
                'death': death,
                'death_increase': death_increase
            }