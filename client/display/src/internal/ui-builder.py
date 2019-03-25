from PIL import Image,ImageDraw,ImageFont

currentlyIconPath = '/Users/nickmarino/weatherbox/client/display/resources/icons/currently/'

class DatePanel:
    PANEL_POSITION = (0, 0)
    SIZE = (400, 30)
    FONT = ImageFont.truetype('Roboto-Medium.ttf', 15)

class CurrentPanel:
    PANEL_POSITION = (0, 31)
    SIZE = (280, 94)

    class IconPanel:
        PANEL_POSITION = (0, 0)
        SIZE = (90, 95)
        ICON_POSITION = (10, 5)
    class ConditionsPanel:
        PANEL_POSITION = (90, 30)
        SIZE = (190, 30)
        TEMP_FONT = ImageFont.truetype('Roboto-Medium.ttf', 35)
    
class UIBuilder:
    def __init__(self, baseUi):
        self.ui = Image.open(baseUi)

    def date(self, date):
        panel = self._createPanel(DatePanel.SIZE) 
        ImageDraw.Draw(panel).text((5,6), date, fill='black', font=DatePanel.FONT)
        self.ui.paste(panel, DatePanel.PANEL_POSITION, panel)
        return self

    def currently(self, currentForecast):
        panel = self._createPanel(CurrentPanel.SIZE)

        icon = self._currentlyIcon(currentForecast['currently']['icon'])
        panel.paste(icon, CurrentPanel.IconPanel.PANEL_POSITION, icon)

        self.ui.paste(panel, CurrentPanel.PANEL_POSITION, panel)
        self.ui.show()
                
    def _currentlyIcon(self, iconProp):
        panel = self._createPanel(CurrentPanel.IconPanel.SIZE)

        icon = self._getIcon(iconProp)
        panel.paste(icon, CurrentPanel.IconPanel.ICON_POSITION, icon)

        return panel
    
    # def _currentlyConditions(self, conditions):
    #     panel = self._createPanel(CurrentPanel.ConditionsPanel.SIZE)

    #     return        
        
    def _createPanel(self, size):
        return Image.new('RGBA', size, (255, 255, 255))

    def _getIcon(self, icon):
        if icon == 'clear-day':
            return Image.open(currentlyIconPath + 'clear-day.png')
        if icon == 'clear-night':
            return Image.open(currentlyIconPath + 'clear-night.png') 
        if icon == 'rain':
            return Image.open(currentlyIconPath + 'rain.png')
        if icon == 'snow':
            return Image.open(currentlyIconPath + 'snow.png')
        if icon == 'sleet':
            return Image.open(currentlyIconPath + 'sleet.png')
        if icon == 'wind':
            return Image.open(currentlyIconPath + 'wind.png')
        if icon == 'fog':
            return Image.open(currentlyIconPath + 'fog.png')
        if icon == 'cloudy':
            return Image.open(currentlyIconPath + 'cloudy.png')
        if icon == 'partly-cloudy-day':
            return Image.open(currentlyIconPath + 'partly-cloudy-day.png')
        if icon == 'partly-cloudy,night':
            return Image.open(currentlyIconPath + 'partly-cloudy-night.png')
        if icon == 'thunderstorm':
            return Image.open(currentlyIconPath + 'thunderstorm')

    



UIBuilder("/Users/nickmarino/weatherbox/client/display/resources/UI.png").date("janlajsdlkfjsdf").currently({"latitude":37.8267,"longitude":-122.4233,"timezone":"America/Los_Angeles","currently":{"time":1551195731,"summary":"Light Rain","icon":"rain","nearestStormDistance":0,"precipIntensity":0.0342,"precipIntensityError":0.0114,"precipProbability":1,"precipType":"rain","temperature":53.26,"apparentTemperature":53.26,"dewPoint":49.28,"humidity":0.86,"pressure":1013.19,"windSpeed":13.15,"windGust":24.85,"windBearing":164,"cloudCover":1,"uvIndex":0,"visibility":6.78,"ozone":278.39},"flags":{"sources":["nearest-precip","cmc","gfs","hrrr","icon","isd","madis","nam","sref","darksky"],"nearest-station":1.839,"units":"us"},"offset":-8})