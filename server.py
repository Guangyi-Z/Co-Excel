#!/usr/bin/python

import BaseHTTPServer
import CGIHTTPServer
import os

import read_conf

keep_serving= True

def serve_not_forever():
    """
        this server keeps serving until stop_server() is called
    """
    ip= read_conf.read_config('ip')
    port= (int) (read_conf.read_config('port'))

    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = (ip, port) # stay empty for localhost ip
    handler.cgi_directories = ["/cgi-bin"]

    httpd = server(server_address, handler)
    while keep_serving:
        httpd.handle_request()

def stop_server():
    global keep_serving
    keep_serving= False

if __name__ == '__main__':
    serve_not_forever()