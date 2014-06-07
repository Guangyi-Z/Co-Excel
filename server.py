#!/usr/bin/python

import BaseHTTPServer
import CGIHTTPServer

keep_serving= True

def serve_not_forever():
    """
        this server keeps serving until stop_server() is called
    """

    port= 8001
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ("", port) # stay empty for localhost ip
    handler.cgi_directories = ["/cgi-bin"]

    httpd = server(server_address, handler)
    while keep_serving:
        httpd.handle_request()

def stop_server():
    global keep_serving
    keep_serving= False

if __name__ == '__main__':
    serve_not_forever()