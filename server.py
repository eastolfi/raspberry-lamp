import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
protocol = "HTTP/1.0"

if sys.argv[1:]:
	port = int(sys.arg[1])
else:
	port = 8001

server_address = ("0.0.0.0", port)

HandlerClass.protocol_version = protocol

httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()

print "Serving HTTP on", sa[0], "port", sa[1], "..."

httpd.serve_forever()
