#!/usr/bin/python

import BaseHTTPServer
import CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8001)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()