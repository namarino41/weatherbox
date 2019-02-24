from PIL import Image,ImageDraw,ImageFont
import yaml

ui_config = './config/ui-config.yaml'

class UIBuilder:
    def __init__(self, baseUi):
        self.ui = Image.open(baseUi)
        self.uiEditor = ImageDraw.Draw(self.ui)

        with open(ui_config, 'r') as stream:
            try: 
                config = yaml.load(stream)
                self.date_config = config['date']
                self.current_config = config['current']
            except yaml.YAMLError as exc:
                print(exc)

    def date(self, date):
        position_config = self.date_config['position']
        font_config = self.date_config['font']

        position = (position_config['x'], position_config['y'])
        font = ImageFont.truetype(font_config['font'], font_config['font-size'])
        self.uiEditor.text(position, date, font=font)
        return self 

