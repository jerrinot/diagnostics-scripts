#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os
import urllib2


PORT = 5701

os.chdir('./plots')
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

response = urllib2.urlopen('http://ipinfo.io/ip')
ip = response.read().rstrip()

print "Serving at http://" + ip + ":" + str(PORT)
httpd.serve_forever()
