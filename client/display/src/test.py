# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont

image = Image.open("/Users/nickmarino/weatherbox/client/display/resources/UI.png")
draw = ImageDraw.Draw(image)
image2 = Image.open("/Users/nickmarino/weatherbox/client/display/resources/icons/current/day-partly-cloudy.png")
h,w = image2.size
image.paste(image2, (10, 35), image2)
font_path = "Roboto-Medium.ttf"
font_path_2 = "/Users/nickmarino/Library/Fonts/Roboto-Light.ttf"
font = ImageFont.truetype(font_path, 35)
font2 = ImageFont.truetype(font_path, 15)
font3 = ImageFont.truetype(font_path, 15)
font4 = ImageFont.truetype(font_path, 11)
draw.text((5, 5), "Thursday, February, 14 2019", font=font2)
h1,w1 = draw.textsize("25˚", font=font)
draw.text((90 + (190-h1)/2, 35), "25˚", font=font)
h3,w3 = draw.textsize("Feels like 15˚", font=font4)
draw.text((90 + (190-h3)/2, 70), "Feels like 15˚", font=font4)
h2,w2 = draw.textsize("Partly cloudy", font=font2)
draw.text((90 + (190-h2)/2, 85), "Partly cloudy", font=font2)

h3,w3 = draw.textsize("Humidity: 100%", font=font4)
draw.text((90 + (95-h3)/2, 105), "Humidity: 10%", font=font4) 
h3,w3 = draw.textsize("Wind: 100 mph", font=font4)
draw.text((185 + (95-h3)/2, 105), "Wind: 100 mph", font=font4) 

################################
h, w = draw.textsize("Today", font=font4)
draw.text(((80-h)/2, 130), "Today", font=font4)
test = Image.open("/Users/nickmarino/weatherbox/client/display/resources/icons/daily/fog.png")
image.paste(test, ((80-55)//2, 140), test)
draw.text((20, 190), "45˚ / 22˚", font=font4)
#draw.text((40, 185), "22˚", font=font4)
w,h = draw.textsize("Heavy Rain", font=font4)
draw.text(((80-w)/2, 205), "Heavy Rain", font=font4)

# draw.text((5, 32), "Alert: Winter weather advisory", font=font4)

image.show()