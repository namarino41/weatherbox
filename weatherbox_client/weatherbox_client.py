import requests
import yaml
import os

''' Weatherbox configuration file path '''
weatherbox_config = os.path.join(os.path.dirname(__file__), 'config/weatherbox-config.yaml')

class WeatherboxClient:
    ''' A client for communicating with the Weatherbox service. '''
    
    def __init__(self):
        with open(weatherbox_config, 'r') as stream:
            try: 
                config = yaml.load(stream)
                self.baseEndpoint = config['baseEndpoint']

                self.endpoints = {}
                for ep in config['endpoints']['web']:
                    self.endpoints.update(ep)

                options = {}
                for opt in config['options']:
                    options.update(opt)

                self.clientId = self._subscribe(options)
            except yaml.YAMLError as exc:
                print(exc)
    
    def _subscribe(self, options):
        ''' Subscribes the client to the Weatherbox service '''
        endpoint = self.baseEndpoint + self.endpoints['subscribe']
        clientId = requests.post(endpoint, json=options).text
        return clientId

    def _getForecast(self, forecastType):
        ''' Convenience method for get forecast data '''
        endpoint = self.baseEndpoint + forecastType
        params = {'clientId': self.clientId}
        forecast = requests.get(endpoint, params=params).json()
        return forecast
    
    def getFull(self):
        ''' Gets the full forecast '''
        return self._getForecast(self.endpoints['full'])

    def getCurrently(self):
        ''' Gets the current forecast '''
        return self._getForecast(self.endpoints['currently'])

    def getDaily(self):
        ''' Gets the daily forecast '''
        return self._getForecast(self.endpoints['daily'])

    def getMinutely(self):
        ''' Gets the minutely forecast '''
        return self._getForecast(self.endpoints['minutely'])
    
    def getHourly(self):
        ''' Gets the hourly forecast '''
        return self._getForecast(self.endpoints['hourly'])

    def getAlerts(self):
        ''' Gets the alerts '''
        return self._getForecast(self.endpoints['alerts'])
