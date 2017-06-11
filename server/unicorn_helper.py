import unicornhat as unicorn

class UnicornHelper:
    def setup(self):
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.2)
        
        width, height = unicorn.get_shape()
        self.width = width
        self.height = height
        
        self.maxBright = 0.9
        self.lowerBright = 0.2
        
    def hexToRGB(self, hex):
        hex = hex.lstrip('#')
        lv = len(hex)
        
        return tuple(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
    def setColorRGB(self, red, green, blue):
        for x in range(self.width):
            for y in range(self.height):
                unicorn.set_pixel(x, y, red, green, blue)
    
        unicorn.show()
        
    def setColorHEX(self, hex):
        r, g, b = self.hexToRGB(hex)
        
        self.setColorRGB(r, g, b)
        
    def addBrightness(self, bright = 2, increase = True):
        current = unicorn.get_brightness()
        
        bright = bright / 10
        
        if increase == False:
            bright = bright * -1
            
        current += bright
        
        if current > self.maxBright:
            current = self.maxBright
        elif current < self.lowerBright:
            current = self.lowerBright
            
        unicorn.brightness(bright)
        unicorn.show()