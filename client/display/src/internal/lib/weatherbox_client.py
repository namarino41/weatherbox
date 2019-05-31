import requests
import yaml

''' Weatherbox configuration file path '''
weatherbox_config = 'internal/config/weatherbox-config.yaml'

''' Weatherbox Enpoints '''
subscribe = '/web/subscribe'
full = '/web/getFull'
currently = '/web/getCurrently'
minutely = '/web/getMinutely'
hourly = '/web/getHourly'
daily = '/web/getDaily'
alerts = '/web/getAlerts'

class WeatherboxClient:
    ''' A client for communicating with the Weatherbox service. '''
    
    def __init__(self):
        with open(weatherbox_config, 'r') as stream:
            try: 
                config = yaml.load(stream)
                self.endpoint = config['endpoint']

                options = {}
                for opt in config['options']:
                    options.update(opt)

                self.clientId = self._subscribe(options)
            except yaml.YAMLError as exc:
                print(exc)
    
    def _subscribe(self, options):
        ''' Subscribes the client to the Weatherbox service '''
        endpoint = self.endpoint + subscribe
        clientId = requests.post(endpoint, json=options).text
        return clientId

    def _getForecast(self, forecastType):
        ''' Convenience method for get forecast data '''
        endpoint = self.endpoint + forecastType
        params = {'clientId': self.clientId}
        forecast = requests.get(endpoint, params=params).json()
        return forecast
    
    def getFull(self):
        ''' Gets the full forecast '''
        return self._getForecast(full)

    def getCurrently(self):
        ''' Gets the current forecast '''
        return self._getForecast(currently)

    def getMinutely(self):
        ''' Gets the minutely forecast '''
        return self._getForecast(minutely)
    
    def getHourly(self):
        ''' Gets the hourly forecast '''
        return self._getForecast(hourly)

    def getAlerts(self):
        ''' Gets the alerts '''
        return self._getForecast(alerts)