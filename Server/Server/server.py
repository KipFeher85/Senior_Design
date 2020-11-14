from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import os
import json



class S(BaseHTTPRequestHandler):

    def do_GET(self):
        rootdir = os.getcwd()

        try:
            print(rootdir + self.path)

            path = self.path.split("?", 1)[0]
            if path == '/':
                self.path += 'Home.html'  # default to Home.html
            if path == '/games':
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.path += "Game.html"
            elif self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.csv'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/csv")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.js'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.json'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.py'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            else:
                self.send_error(404, 'file not supported')

        except IOError:
            self.send_error(404, 'file not found')

    def do_POST(self):
        rootdir = os.getcwd()

        try:
            print(rootdir + self.path)

            path = self.path.split("?", 1)[0]

            # handle 'addone' endpoint
            if path == '/addone':

                # JSON string
                payloadString = self.rfile.read(int(self.headers['Content-Length']))

                # Python dictionary
                payload = json.loads(payloadString)

                number = int(payload['number'])

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                # call the prediction function in ml.py
                result = number

                # make a Python dictionary from the result
                resultObj = {"number": result}

                # convert Python dictionary to JSON string
                resultString = json.dumps(resultObj)

                self.wfile.write(resultString.encode('utf-8'))

            else:
                self.send_error(404, 'endpoint not supported')

        except IOError:
            self.send_error(404, 'endpoint not found')


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)