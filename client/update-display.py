#!/usr/bin/python
# -*- coding:utf-8 -*-

from display.lib import epd4in2
from display.lib import ui_builder
from weatherbox.lib import weatherbox_client
from datetime import datetime
import sys
sys.path.append('display/')
sys.path.append('weatherbox/')

if __name__ == '__main__':
    global weatherboxClient
    weatherboxClient = weatherbox_client.WeatherboxClient()

def updateDisplay():
    forecast = weatherboxClient.getFull()

    currently_forecast = forecast['currently']
    daily_forecast = forecast['daily']
    hourly_forecast = forecast['hourly']

    ui = ui_builder.UIBuilder() \
        .date(datetime.today()) \
        .currently(currently_forecast) \
        .daily(daily_forecast) \
        .hourly(hourly_forecast) \
        .build()

    epd = epd4in2.EPD()
    epd.init()
    epd.Clear(0xFF)
    epd.display(epd.getbuffer(ui))
    epd.sleep()

    # ui.show()

updateDisplay()
