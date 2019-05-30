# -*- coding: utf-8 -*-
import json
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

baseUi = '/Users/nickmarino/weatherbox/client/display/assets/UI.png'
currentlyIconPath = '/Users/nickmarino/weatherbox/client/display/assets/icons/currently/'
dailyIconPath = '/Users/nickmarino/weatherbox/client/display/assets/icons/daily/'
hourlyIconPath = '/Users/nickmarino/weatherbox/client/display/assets/icons/hourly/'


# class DatePanel:
#     PANEL_POSITION = (0, 0)
#     SIZE = (400, 30)

#     DATE_POSITION = (5,6)
#     FONT = ImageFont.truetype('Roboto-Medium.ttf', 15)

# class CurrentlyPanel:
#     PANEL_POSITION = (0, 31)
#     SIZE = (280, 94)

#     class IconPanel:
#         PANEL_POSITION = (0, 0)
#         SIZE = (90, 95)
#         ICON_POSITION = (10, 5)
#     class ConditionsPanel:
#         PANEL_POSITION = (90, 0)
#         SIZE = (190, 95)

#         TEMP_POSITION_Y = 5
#         TEMP_FONT = ImageFont.truetype('Roboto-Medium.ttf', 35)

#         FEELS_LIKE_POSITION_Y = 40
#         FEELS_LIKE_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

#         SUMMARY_POSITION_Y = 55
#         SUMMARY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 15)

#         HUMIDITY_POSITION_Y = 75
#         HUMIDITY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

#         WIND_POSITION_Y = 75
#         HUMIDITY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

# class DailyPanel:
#     PANEL_POSITION = (0, 126)
#     SIZE = (79, 99)

#     DAY_LOCATION_Y = 5
#     DAY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

#     ICON_POSITION_Y= 15

#     TEMP_POSITION_Y = 65
#     TEMP_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

#     SUMMARY_POSITION_Y = 80
#     SUMMARY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)


class UIBuilder:
    def __init__(self):
        self.ui = Image.open(baseUi)

    def date(self, date):
        panel = self._createPanel((400, 30)) 
        ImageDraw.Draw(panel).text((5,6), date, fill='black', \
            font=ImageFont.truetype('Roboto-Medium.ttf', 15))
        self.ui.paste(panel, (0, 0), panel)

        return self

    def currently(self, currentlyForecast):
        panel = self._createPanel((280, 94))

        conditions = self._currently(currentlyForecast)
        panel.paste(conditions, (0, 0), conditions)

        self.ui.paste(panel, (0, 31), panel)

        return self

    def daily(self, dailyForecast):
        for i in range(0, 5):
            panel = self._daily(dailyForecast['data'][i])
            self.ui.paste(panel, ((80 * i), 126), panel)

        return self

    def hourly(self, hourlyForecast):
        for i in range(0, 5):
            hourlyForecast['data'][i]
            panel = self._hourly(hourlyForecast['data'][i])
            self.ui.paste(panel, ((80 * i), 226), panel)
        self.ui.show()

        return self
 
    def _hourly(self, conditions):
        panel = self._createPanel((79, 99))
        draw = ImageDraw.Draw(panel)

        time = datetime.fromtimestamp(conditions['time']).hour
        
        if (time > 12):
            time = str((time % 12)) + ' PM'
        else:
            time = str(time) + ' AM'

        h,w = draw.textsize("{}".format(time), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text((((79 - h) / 2), 2), time, fill='black', \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        icon = self._getIcon('daily', conditions['icon'])
        panel.paste(icon, ((80-55)//2, 9), icon)

        temp = int(conditions['temperature'])
        feelsLike = int(conditions['apparentTemperature'])

        h,w = draw.textsize("{}\xb0/{}\xb0".format(temp, feelsLike), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text(((79-h)/2, 58), "{}\xb0/{}\xb0".format(temp, feelsLike), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        return panel

    def _currently(self, conditions):
        panel = self._createPanel((280, 95))
        draw = ImageDraw.Draw(panel)

        icon = self._getIcon('currently', conditions['icon'])
        panel.paste(icon, (10, 5), icon)
        
        temperature = str(int(conditions['temperature']))
        feelsLike = str(int(conditions['apparentTemperature']))
        summary = conditions['summary']
        humidity = str(int(conditions['humidity'] * 100))
        wind = str(int(conditions['windGust']))

        # Draw temperature.
        h,w = draw.textsize("{}\xb0".format(temperature), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 35))
        draw.text((90 + (190 - h)/ 2, 5), "{}\xb0".format(temperature), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 35))

        # Draw 'feels like' temperature.
        h,w = draw.textsize("Feels like {}\xb0".format(feelsLike), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text((90 + (190 - h)/ 2, 40), "Feels like {}\xb0".format(feelsLike), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        # Draw summary.
        h,w = draw.textsize("{}".format(summary), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 15))
        draw.text((90 + (190 - h) / 2, 55), "{}".format(summary), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 15))

        # Draw humidity.
        h,w = draw.textsize("Humidity: {}%".format(humidity), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text(((180 + (190 / 2) - h) / 2, 75), "Humidity: {}%".format(humidity), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        # Draw wind.
        h,w = draw.textsize("Wind: {} mph".format(wind), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text((90 + (190 / 2) + ((190 / 2) - h) / 2, 75), "Wind: {} mph".format(wind), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        return panel

    def _daily(self, conditions):
        panel = self._createPanel((79, 99))
        draw = ImageDraw.Draw(panel)
        
        day = datetime.fromtimestamp(\
            conditions['time']).strftime("%A")
        h,w = draw.textsize("{}".format(day), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text((((79 - h) / 2), 5), day, fill='black', \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        
        icon = self._getIcon('daily', conditions['icon'])
        panel.paste(icon, ((80-55)//2, 15), icon)

        highTemp = int(conditions['temperatureHigh'])
        lowTemp = int(conditions['temperatureLow'])

        h,w = draw.textsize("{}\xb0/{}\xb0".format(highTemp, lowTemp), \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))
        draw.text(((79-h)/2, 65), "{}\xb0/{}\xb0".format(lowTemp, highTemp), \
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))         

        h,w = draw.textsize(conditions['summary'], \
            font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        if h > 79:
            h,w = draw.textsize(self._getSummaryFromIcon(conditions['icon']), \
                font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        draw.text(((79-h)/2, 80), self._getSummaryFromIcon(conditions['icon']),
            fill='black', font=ImageFont.truetype('Roboto-Medium.ttf', 11))

        return panel

    def _getIcon(self, type, icon):
        if type == 'currently':
            iconPath = currentlyIconPath
        elif type == 'daily':
            iconPath = dailyIconPath
        elif type == 'hourly':
            iconPath = hourlyIconPath

        if icon == 'clear-day':
            return Image.open(iconPath + 'clear-day.png')
        if icon == 'clear-night':
            return Image.open(iconPath + 'clear-night.png') 
        if icon == 'rain':
            return Image.open(iconPath + 'rain.png')
        if icon == 'snow':
            return Image.open(iconPath + 'snow.png')
        if icon == 'sleet':
            return Image.open(iconPath + 'sleet.png')
        if icon == 'wind':
            return Image.open(iconPath + 'wind.png')
        if icon == 'fog':
            return Image.open(iconPath + 'fog.png')
        if icon == 'cloudy':
            return Image.open(iconPath + 'cloudy.png')
        if icon == 'partly-cloudy-day':
            return Image.open(iconPath + 'partly-cloudy-day.png')
        if icon == 'partly-cloudy-night':
            return Image.open(iconPath + 'partly-cloudy-night.png')
        if icon == 'thunderstorm':
            return Image.open(iconPath + 'thunderstorm')

    def _getSummaryFromIcon(self, icon):
        if icon == 'clear-day':
            return 'Clear'
        if icon == 'clear-night':
            return 'Clear'
        if icon == 'rain':
            return 'Rain'
        if icon == 'snow':
            return 'Snow'
        if icon == 'sleet':
            return 'Sleet'
        if icon == 'wind':
            return 'Wind'
        if icon == 'fog':
            return 'Fog'
        if icon == 'cloudy':
            return 'Cloudy'
        if icon == 'partly-cloudy-day':
            return 'Partly Cloudy'
        if icon == 'partly-cloudy-night':
            return 'Partly Cloudy'
        if icon == 'thunderstorm':
            return 'Thunderstorm'

    def _createPanel(self, size):
        return Image.new('RGBA', size, (255, 255, 255))
    

with open("/Users/nickmarino/Downloads/test.json") as file:
    data = json.load(file)
    UIBuilder().date(datetime.today().strftime('%Y-%m-%d')).currently(data['currently']).daily(data['daily']).hourly(data['hourly'])