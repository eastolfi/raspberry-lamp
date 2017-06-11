#!env/bin/python
import os
import math
from flask import Flask
from flask_restful import Resource, Api
from .unicorn_helper import UnicornHelper

app = Flask(__name__)
api = Api(app)

unicornHelper = UnicornHelper()

# @app.route("/")
# @app.route("/index")
# def index():
# 	print "index"
# 	return "index"
	
# @app.route("/color/<hex>")
# def color(hex):
#     print hex

# unicornHelper.setColorRGB(255, 0, 255)
# elif self.path == "/rojo":
#     # unicornHelper.setColorRGB(255, 0, 0)
# elif self.path == "/addBright":
#     unicornHelper.addBrightness()
# elif self.path == "/lessBright":
#     unicornHelper.addBrightness(increase = False)
# elif self.path == "/off":
#     unicornHelper.off()

class ColorHelper:
    def _hexToRGB(self, hex):
        hex = hex.lstrip('#')
        lv = len(hex)
        
        return tuple(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        
    def get(self, color):
        if color[0] == "#":
            return { "color": color }
        else:
            return { "color": color }
            
class ColorHex(Resource):
    def get(self, hex):
        # unicornHelper.setColorRGB(255, 0, 0)
        return { "hex": hex }

class ColorRGB(Resource):
    def get(self, red, green, blue):
        # unicornHelper.setColorRGB(255, 0, 0)
        return { "rgb": red + green + blue }
        
class Brightness(Resource):
    def get(self, bright, increase):
        bright = int(bright)
        
        if bright > 1:
            bright = math.ceil(bright) / 10
        
        if increase == "N":
            bright = bright * -1
            
        unicornHelper.addBrightness(bright = bright)
        
        return { "bright": bright }
        
api.add_resource(ColorHex, "/color/<string:hex>")
api.add_resource(ColorRGB, "/color/<string:red>/<string:green>/<string:blue>")
api.add_resource(Brightness, "/bright/<string:bright>/<string:increase>")

app.run(host = os.getenv("IP", "0.0.0.0"), port = 3000)