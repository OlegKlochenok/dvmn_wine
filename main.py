# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from http.server import HTTPServer, SimpleHTTPRequestHandler


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
