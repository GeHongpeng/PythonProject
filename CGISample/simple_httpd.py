import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = "."
port = 8081

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(srvrobj.server_port))
srvrobj.serve_forever()

