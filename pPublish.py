#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os
import urllib2


PORT = 5701
PLOT_DIRECTORY = './plots'


def get_external_ip():
    response = urllib2.urlopen('http://ipinfo.io/ip')
    ip = response.read().rstrip()
    return ip

os.chdir(PLOT_DIRECTORY)
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

external_ip = get_external_ip()
port_string = str(PORT)

print "Serving at http://" + external_ip + ":" + port_string
print "If you are working locally then you can try http://127.0.0.1:" + port_string
httpd.serve_forever()