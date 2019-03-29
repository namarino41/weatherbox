# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

baseUi = '/Users/nickmarino/weatherbox/client/display/resources/UI.png'
currentlyIconPath = '/Users/nickmarino/weatherbox/client/display/resources/icons/currently/'
dailyIconPath = '/Users/nickmarino/weatherbox/client/display/resources/icons/daily/'


class DatePanel:
    PANEL_POSITION = (0, 0)
    SIZE = (400, 30)

    DATE_POSITION = (5,6)
    FONT = ImageFont.truetype('Roboto-Medium.ttf', 15)

class CurrentlyPanel:
    PANEL_POSITION = (0, 31)
    SIZE = (280, 94)

    class IconPanel:
        PANEL_POSITION = (0, 0)
        SIZE = (90, 95)
        ICON_POSITION = (10, 5)
    class ConditionsPanel:
        PANEL_POSITION = (90, 0)
        SIZE = (190, 95)

        TEMP_POSITION_Y = 5
        TEMP_FONT = ImageFont.truetype('Roboto-Medium.ttf', 35)

        FEELS_LIKE_POSITION_Y = 40
        FEELS_LIKE_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

        SUMMARY_POSITION_Y = 55
        SUMMARY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 15)

        HUMIDITY_POSITION_Y = 75
        HUMIDITY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

        WIND_POSITION_Y = 75
        HUMIDITY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

class DailyPanel:
    PANEL_POSITION = (0, 126)
    SIZE = (79, 99)

    DAY_LOCATION_Y = 5
    DAY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

    ICON_POSITION_Y= 15

    TEMP_POSITION_Y = 65
    TEMP_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)

    SUMMARY_POSITION_Y = 80
    SUMMARY_FONT = ImageFont.truetype('Roboto-Medium.ttf', 11)


class UIBuilder:
    def __init__(self):
        self.ui = Image.open(baseUi)

    def date(self, date):
        panel = self._createPanel(DatePanel.SIZE) 
        ImageDraw.Draw(panel).text(DatePanel.DATE_POSITION, date, fill='black', font=DatePanel.FONT)
        self.ui.paste(panel, DatePanel.PANEL_POSITION, panel)
        return self

    def currently(self, currentlyForecast):
        panel = self._createPanel(CurrentlyPanel.SIZE)

        icon = self._currentlyIcon(currentlyForecast['currently']['icon'])
        panel.paste(icon, CurrentlyPanel.IconPanel.PANEL_POSITION, icon)

        conditions = self._currentlyConditions(currentlyForecast['currently'])
        panel.paste(conditions, CurrentlyPanel.ConditionsPanel.PANEL_POSITION, conditions)

        self.ui.paste(panel, CurrentlyPanel.PANEL_POSITION, panel)
        self.ui.show()
        return self

    def daily(self, dailyForecast):
        for i in range(0, 5):
            panel = self._createPanel(DailyPanel.SIZE)
            draw = ImageDraw.Draw(panel)
            
            day = datetime.fromtimestamp( \
                dailyForecast['daily']['data'][i]['time']).strftime("%A")
            h,w = draw.textsize("{}".format(day), \
                font=DailyPanel.DAY_FONT)
            draw.text((((DailyPanel.SIZE[0] - h) / 2), DailyPanel.DAY_LOCATION_Y), \
                day, fill='black', font=DailyPanel.DAY_FONT)
             
            icon = self._getIcon('daily', dailyForecast['daily']['data'][i]['icon'])
            panel.paste(icon, ((80-55)//2, DailyPanel.ICON_POSITION_Y), icon)

            highTemp = int(dailyForecast['daily']['data'][i]['temperatureHigh'])
            lowTemp = int(dailyForecast['daily']['data'][i]['temperatureLow'])

            h,w = draw.textsize("{}˚/{}˚".format(highTemp, lowTemp), \
                font=DailyPanel.TEMP_FONT)
            draw.text(((79-h)/2, DailyPanel.TEMP_POSITION_Y), "{}˚/{}˚".format(lowTemp, highTemp), fill='black', font=DailyPanel.TEMP_FONT)
            
            h,w = draw.textsize("Clear", \
                font=DailyPanel.TEMP_FONT)
            draw.text(((79-h)/2, DailyPanel.SUMMARY_POSITION_Y), "Clear", fill='black', font=DailyPanel.TEMP_FONT)


            self.ui.paste(panel, \
                (DailyPanel.PANEL_POSITION[0] + (80 * i), DailyPanel.PANEL_POSITION[1]), panel)

        self.ui.show()
            



        
    def _currentlyIcon(self, iconProp):
        iconPanel = CurrentlyPanel.IconPanel

        panel = self._createPanel(iconPanel.SIZE)

        icon = self._getIcon('currently', iconProp)
        panel.paste(icon, iconPanel.ICON_POSITION, icon)

        return panel

    def _currentlyConditions(self, conditions):
        conditionsPanel = CurrentlyPanel.ConditionsPanel
        conditionsPanelSize = conditionsPanel.SIZE

        panel = self._createPanel(conditionsPanel.SIZE)
        draw = ImageDraw.Draw(panel)
        
        temperature = str(int(conditions['temperature']))
        feelsLike = str(int(conditions['apparentTemperature']))
        summary = conditions['summary']
        humidity = str(int(conditions['humidity'] * 100))
        wind = str(int(conditions['windGust']))

        # Draw temperature.
        h,w = draw.textsize("{}˚".format(temperature), \
            font=conditionsPanel.TEMP_FONT)
        draw.text(((conditionsPanelSize[0] - h) / 2, conditionsPanel.TEMP_POSITION_Y), \
            "{}˚".format(temperature), fill='black', font=conditionsPanel.TEMP_FONT)
        
        # Draw 'feels like' temperature.
        h,w = draw.textsize("Feels like {}˚".format(feelsLike), \
            font=conditionsPanel.FEELS_LIKE_FONT)
        draw.text(((conditionsPanelSize[0] - h) / 2, conditionsPanel.FEELS_LIKE_POSITION_Y), \
            "Feels like {}˚".format(feelsLike), fill='black', font=conditionsPanel.FEELS_LIKE_FONT)

        # Draw summary.
        h,w = draw.textsize("{}".format(summary), \
            font=conditionsPanel.SUMMARY_FONT)
        draw.text(((conditionsPanelSize[0] - h) / 2, conditionsPanel.SUMMARY_POSITION_Y), \
            "{}".format(summary), fill='black', font=conditionsPanel.SUMMARY_FONT)

        # Draw humidity.
        h,w = draw.textsize("Humidity: {}%".format(humidity), \
            font=conditionsPanel.FEELS_LIKE_FONT)
        draw.text((((conditionsPanelSize[0] / 2) - h) / 2, conditionsPanel.HUMIDITY_POSITION_Y), \
            "Humidity: {}%".format(humidity), fill='black', font=conditionsPanel.FEELS_LIKE_FONT)

        # Draw wind.
        h,w = draw.textsize("Wind: {} mph".format(wind), \
            font=conditionsPanel.FEELS_LIKE_FONT)
        draw.text(((conditionsPanelSize[0] / 2) + ((conditionsPanelSize[0] / 2) - h) / 2, conditionsPanel.WIND_POSITION_Y), \
            "Wind: {} mph".format(wind), fill='black', font=conditionsPanel.FEELS_LIKE_FONT)

        return panel

    def _getIcon(self, type, icon):
        if type == 'currently':
            iconPath = currentlyIconPath
        elif type == 'daily':
            iconPath = dailyIconPath

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
        if icon == 'partly-cloudy,night':
            return Image.open(iconPath + 'partly-cloudy-night.png')
        if icon == 'thunderstorm':
            return Image.open(iconPath + 'thunderstorm')

    def _createPanel(self, size):
        return Image.new('RGBA', size, (255, 255, 255))
    

test = {"latitude":37.8267,"longitude":-122.4233,"timezone":"America/Los_Angeles","daily":{"summary":"No precipitation throughout the week, with high temperatures peaking at 67°F on Monday.","icon":"clear-day","data":[{"time":1553756400,"summary":"Partly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1553781720,"sunsetTime":1553826583,"moonPhase":0.77,"precipIntensity":0.0023,"precipIntensityMax":0.008,"precipIntensityMaxTime":1553778000,"precipProbability":0.57,"precipType":"rain","temperatureHigh":57.94,"temperatureHighTime":1553806800,"temperatureLow":49.4,"temperatureLowTime":1553868000,"apparentTemperatureHigh":57.94,"apparentTemperatureHighTime":1553806800,"apparentTemperatureLow":49.22,"apparentTemperatureLowTime":1553871600,"dewPoint":46.78,"humidity":0.74,"pressure":1023.07,"windSpeed":6.35,"windGust":19.03,"windGustTime":1553810400,"windBearing":219,"cloudCover":0.5,"uvIndex":5,"uvIndexTime":1553803200,"visibility":8.78,"ozone":342.75,"temperatureMin":52.28,"temperatureMinTime":1553839200,"temperatureMax":57.94,"temperatureMaxTime":1553806800,"apparentTemperatureMin":52.28,"apparentTemperatureMinTime":1553839200,"apparentTemperatureMax":57.94,"apparentTemperatureMaxTime":1553806800},{"time":1553842800,"summary":"Partly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1553868028,"sunsetTime":1553913038,"moonPhase":0.8,"precipIntensity":0.0006,"precipIntensityMax":0.0079,"precipIntensityMaxTime":1553842800,"precipProbability":0.26,"precipType":"rain","temperatureHigh":59.77,"temperatureHighTime":1553896800,"temperatureLow":49.33,"temperatureLowTime":1553954400,"apparentTemperatureHigh":59.77,"apparentTemperatureHighTime":1553896800,"apparentTemperatureLow":49.07,"apparentTemperatureLowTime":1553950800,"dewPoint":45.28,"humidity":0.73,"pressure":1027.77,"windSpeed":5.55,"windGust":15.87,"windGustTime":1553914800,"windBearing":299,"cloudCover":0.25,"uvIndex":6,"uvIndexTime":1553889600,"visibility":10,"ozone":335.14,"temperatureMin":49.4,"temperatureMinTime":1553868000,"temperatureMax":59.77,"temperatureMaxTime":1553896800,"apparentTemperatureMin":49.22,"apparentTemperatureMinTime":1553871600,"apparentTemperatureMax":59.77,"apparentTemperatureMaxTime":1553896800},{"time":1553929200,"summary":"Partly cloudy until afternoon.","icon":"partly-cloudy-day","sunriseTime":1553954336,"sunsetTime":1553999492,"moonPhase":0.83,"precipIntensity":0.0002,"precipIntensityMax":0.0006,"precipIntensityMaxTime":1553954400,"precipProbability":0.08,"precipType":"rain","temperatureHigh":60.96,"temperatureHighTime":1553986800,"temperatureLow":52.09,"temperatureLowTime":1554040800,"apparentTemperatureHigh":60.96,"apparentTemperatureHighTime":1553986800,"apparentTemperatureLow":52.09,"apparentTemperatureLowTime":1554040800,"dewPoint":46.02,"humidity":0.73,"pressure":1025.13,"windSpeed":4.36,"windGust":11.06,"windGustTime":1553994000,"windBearing":294,"cloudCover":0.26,"uvIndex":6,"uvIndexTime":1553976000,"visibility":10,"ozone":336.14,"temperatureMin":49.33,"temperatureMinTime":1553954400,"temperatureMax":60.96,"temperatureMaxTime":1553986800,"apparentTemperatureMin":49.07,"apparentTemperatureMinTime":1553950800,"apparentTemperatureMax":60.96,"apparentTemperatureMaxTime":1553986800},{"time":1554015600,"summary":"Partly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1554040645,"sunsetTime":1554085946,"moonPhase":0.86,"precipIntensity":0.0004,"precipIntensityMax":0.0009,"precipIntensityMaxTime":1554040800,"precipProbability":0.08,"precipType":"rain","temperatureHigh":66,"temperatureHighTime":1554073200,"temperatureLow":55.02,"temperatureLowTime":1554127200,"apparentTemperatureHigh":66,"apparentTemperatureHighTime":1554073200,"apparentTemperatureLow":55.02,"apparentTemperatureLowTime":1554127200,"dewPoint":48.29,"humidity":0.71,"pressure":1022.54,"windSpeed":3.53,"windGust":12.75,"windGustTime":1554080400,"windBearing":285,"cloudCover":0.37,"uvIndex":6,"uvIndexTime":1554062400,"visibility":10,"ozone":318.7,"temperatureMin":52.09,"temperatureMinTime":1554040800,"temperatureMax":66,"temperatureMaxTime":1554073200,"apparentTemperatureMin":52.09,"apparentTemperatureMinTime":1554040800,"apparentTemperatureMax":66,"apparentTemperatureMaxTime":1554073200},{"time":1554102000,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1554126953,"sunsetTime":1554172401,"moonPhase":0.89,"precipIntensity":0.0001,"precipIntensityMax":0.0007,"precipIntensityMaxTime":1554184800,"precipProbability":0.11,"precipType":"rain","temperatureHigh":66.82,"temperatureHighTime":1554152400,"temperatureLow":55.73,"temperatureLowTime":1554206400,"apparentTemperatureHigh":66.82,"apparentTemperatureHighTime":1554152400,"apparentTemperatureLow":55.73,"apparentTemperatureLowTime":1554206400,"dewPoint":51.69,"humidity":0.74,"pressure":1016.98,"windSpeed":3.48,"windGust":11.48,"windGustTime":1554163200,"windBearing":294,"cloudCover":0.76,"uvIndex":5,"uvIndexTime":1554145200,"visibility":9.97,"ozone":312.41,"temperatureMin":55.02,"temperatureMinTime":1554127200,"temperatureMax":66.82,"temperatureMaxTime":1554152400,"apparentTemperatureMin":55.02,"apparentTemperatureMinTime":1554127200,"apparentTemperatureMax":66.82,"apparentTemperatureMaxTime":1554152400},{"time":1554188400,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1554213263,"sunsetTime":1554258855,"moonPhase":0.92,"precipIntensity":0.0021,"precipIntensityMax":0.0058,"precipIntensityMaxTime":1554217200,"precipProbability":0.61,"precipType":"rain","temperatureHigh":57.96,"temperatureHighTime":1554249600,"temperatureLow":53.22,"temperatureLowTime":1554292800,"apparentTemperatureHigh":57.96,"apparentTemperatureHighTime":1554249600,"apparentTemperatureLow":53.22,"apparentTemperatureLowTime":1554292800,"dewPoint":50.72,"humidity":0.82,"pressure":1013.61,"windSpeed":6.23,"windGust":15.84,"windGustTime":1554253200,"windBearing":247,"cloudCover":0.87,"uvIndex":3,"uvIndexTime":1554228000,"visibility":8.73,"ozone":364.58,"temperatureMin":54.06,"temperatureMinTime":1554271200,"temperatureMax":58.44,"temperatureMaxTime":1554188400,"apparentTemperatureMin":54.06,"apparentTemperatureMinTime":1554271200,"apparentTemperatureMax":58.44,"apparentTemperatureMaxTime":1554188400},{"time":1554274800,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1554299572,"sunsetTime":1554345309,"moonPhase":0.95,"precipIntensity":0.0024,"precipIntensityMax":0.005,"precipIntensityMaxTime":1554310800,"precipProbability":0.36,"precipType":"rain","temperatureHigh":58.89,"temperatureHighTime":1554328800,"temperatureLow":52.6,"temperatureLowTime":1554364800,"apparentTemperatureHigh":58.89,"apparentTemperatureHighTime":1554328800,"apparentTemperatureLow":52.6,"apparentTemperatureLowTime":1554364800,"dewPoint":48.23,"humidity":0.78,"pressure":1015.93,"windSpeed":5.89,"windGust":12.31,"windGustTime":1554328800,"windBearing":243,"cloudCover":0.81,"uvIndex":5,"uvIndexTime":1554321600,"visibility":9.07,"ozone":325.66,"temperatureMin":52.82,"temperatureMinTime":1554357600,"temperatureMax":58.89,"temperatureMaxTime":1554328800,"apparentTemperatureMin":52.82,"apparentTemperatureMinTime":1554357600,"apparentTemperatureMax":58.89,"apparentTemperatureMaxTime":1554328800},{"time":1554361200,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1554385882,"sunsetTime":1554431764,"moonPhase":0.98,"precipIntensity":0.0065,"precipIntensityMax":0.0228,"precipIntensityMaxTime":1554411600,"precipProbability":0.89,"precipType":"rain","temperatureHigh":57.12,"temperatureHighTime":1554426000,"temperatureLow":55.83,"temperatureLowTime":1554447600,"apparentTemperatureHigh":57.12,"apparentTemperatureHighTime":1554426000,"apparentTemperatureLow":55.83,"apparentTemperatureLowTime":1554447600,"dewPoint":48.43,"humidity":0.79,"pressure":1016.56,"windSpeed":5.66,"windGust":23.81,"windGustTime":1554426000,"windBearing":168,"cloudCover":0.79,"uvIndex":4,"uvIndexTime":1554404400,"visibility":7.02,"ozone":328.35,"temperatureMin":52.6,"temperatureMinTime":1554364800,"temperatureMax":57.12,"temperatureMaxTime":1554426000,"apparentTemperatureMin":52.6,"apparentTemperatureMinTime":1554364800,"apparentTemperatureMax":57.12,"apparentTemperatureMaxTime":1554426000}]},"flags":{"sources":["cmc","gfs","hrrr","icon","isd","madis","nam","sref"],"nearest-station":1.839,"units":"us"},"offset":-7}


UIBuilder().date("janlajsdlkfjsdf") \
    .daily(test)
# .currently({"latitude":37.8267,"longitude":-122.4233,"timezone":"America/Los_Angeles","currently":{"time":1551195731,"summary":"Light Rain","icon":"rain","nearestStormDistance":0,"precipIntensity":0.0342,"precipIntensityError":0.0114,"precipProbability":1,"precipType":"rain","temperature":53.26,"apparentTemperature":53.26,"dewPoint":49.28,"humidity":0.86,"pressure":1013.19,"windSpeed":13.15,"windGust":24.85,"windBearing":164,"cloudCover":1,"uvIndex":0,"visibility":6.78,"ozone":278.39},"flags":{"sources":["nearest-precip","cmc","gfs","hrrr","icon","isd","madis","nam","sref","darksky"],"nearest-station":1.839,"units":"us"},"offset":-8})