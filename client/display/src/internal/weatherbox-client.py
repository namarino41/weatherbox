
# Facilitates communication between the client and 
# the Weatherbox server.
# import requests
import yaml

weatherbox_config = './config/weatherbox-config.yaml'

class WeatherboxClient:
    def __init__(self):
        with open(weatherbox_config, 'r') as stream:
            try: 
                config = yaml.load(stream)['weatherbox']
                self.endpoint = config['endpoint']
                self.options = config['location']
            except yaml.YAMLError as exc:
                print(exc)





          


