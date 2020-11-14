import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import http.server as httpServer

server = httpServer.HTTPServer
handler = httpServer.CGIHTTPRequestHandler
server_address = ("", 8080)
#This defaults to ['/cgi-bin', '/htbin'] and describes directories to treat as containing CGI scripts
handler.cgi_directories = ["/cgi-bin"]
httpd = server(server_address, handler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()