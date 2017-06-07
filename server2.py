#!/usr/bin/env python

from os import curdir, sep
import unicornhat as unicorn
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.2)

width, height = unicorn.get_shape()

def setColor(red, green, blue):
    for x in range(width):
        for y in range(height):
            unicorn.set_pixel(x, y, red, green, blue)

    unicorn.show()

def incBrightness():
    bright = unicorn.get_brightness()
    bright += 0.2

    if bright > 1.0:
        bright = 1.0
    
    unicorn.brightness(bright)
    unicorn.show()

def decBrightness():
    bright = unicorn.get_brightness()
    bright -= 0.2

    if bright < 0.2:
        bright = 0.2
        
    unicorn.brightness(bright)
    unicorn.show()

class CustomHandler(SimpleHTTPRequestHandler):
    def _set_headers(self, mimetype = "text/html"):
        self.send_response(200)
        self.send_header("Content-type", mimetype)
        self.end_headers()
        
    def _get_mimetype(self):
        if self.path.endswith(".html") or self.path == "/":
            return "text/html"
        elif self.path.endswith(".jpg"):
            return "image/jpg"
        elif self.path.endswith(".gif"):
            return "image/gif"
        elif self.path.endswith(".js"):
            return "application/javascript"
        elif self.path.endswith(".css"):
            return "text/css"
        else:
            return False

    def getPathFileContent(self):
        if self.path == "/":
            path = "index.html"

        f = open(curdir + sep + path)

        return f.read()

    def do_GET(self):
        if self.path == "/morado":
            setColor(255, 0, 255)
        elif self.path == "/rojo":
            setColor(255, 0, 0)
        elif self.path == "/addBright":
            incBrightness()
        elif self.path == "/lessBright":
            decBrightness()
        elif self.path == "/off":
            unicorn.off()
        else:
            mime = self._get_mimetype()

            if mime != False:
                self._set_headers(mime)
            
            fContent = self.getPathFileContent()
            self.wfile.write(fContent)
        
    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST</h1></body></html>")

def serve(ServerClass = BaseHTTPServer.HTTPServer, HandlerClass = CustomHandler, port = 8001):
    protocol = "HTTP/1.0"
    server_address = ("0.0.0.0", port)

    HandlerClass.protocol_version = protocol

    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

def clean():
    unicorn.off()

try:
    if __name__ == "__main__":
        from sys import argv

        if len(argv) == 2:
            serve(port = int(argv[1]))
        else:
            serve()
except Exception as ex:
    print ex
    clean()
