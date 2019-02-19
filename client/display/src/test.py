from PIL import Image,ImageDraw,ImageFont

image = Image.open("/Users/nickmarino/weatherbox/client/display/assets/anotherTestUI.png")
draw = ImageDraw.Draw(image)
image2 = Image.open("/Users/nickmarino/weatherbox/client/display/assets/icons/current/wind.png")
h,w = image2.size
image.paste(image2, (10, 35), image2)
font_path = "/Users/nickmarino/Library/Fonts/Roboto-Medium.ttf"
font_path_2 = "/Users/nickmarino/Library/Fonts/Roboto-Light.ttf"
font = ImageFont.truetype(font_path, 35)
font2 = ImageFont.truetype(font_path, 15)
font3 = ImageFont.truetype(font_path, 15)
font4 = ImageFont.truetype(font_path, 10)
draw.text((5, 5), "Thursday, February, 14, 2019", font=font2)
h1,w1 = draw.textsize("25F", font=font)
draw.text((90 + (190-h1)/2, 35), "25F", font=font)
h3,w3 = draw.textsize("Feels like 15F", font=font4)
draw.text((90 + (190-h3)/2, 70), "Feels like 15F", font=font4)
h2,w2 = draw.textsize("Partly cloudy", font=font2)
draw.text((90 + (190-h2)/2, 85), "Partly cloudy", font=font2)

h3,w3 = draw.textsize("Humidity: 100%", font=font4)
draw.text((90 + (95-h3)/2, 105), "Humidity: 10%", font=font4) 
h3,w3 = draw.textsize("Wind: 100 mph", font=font4)
draw.text((185 + (95-h3)/2, 105), "Wind: 100 mph", font=font4) 

################################
draw.text((5, 130), "Mon", font=font4)
test = Image.open("/Users/nickmarino/weatherbox/client/display/assets/icons/daily/fog.png")
image.paste(test, (5, 135), test)
draw.text((5, 190), "45˚", font=font3)
draw.text((40, 190), "22˚", font=font4)
draw.text((5, 210), "Heavy Rain", font=font4)

image.show()