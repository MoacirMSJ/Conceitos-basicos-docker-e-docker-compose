import os

import http.server
import socketserver

print('O container foi iniciado...')
print('Subindo o servidor')
print('acesse: http://localhost:8000/')

PORT = 8000
name = os.getenv('NAME')

html_content = '<html lang="en"> \
<head> \
  <meta charset="UTF-8"> \
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> \
  <meta name="viewport" content="width=device-width, initial-scale=1.0">\
  <title>Document</title> \
</head>\
<body>\
  <h1>Olá {} </h1>\
</body>\
</html>'.format(name)


f = open("./index.html", "w")
f.write(html_content)
f.close()

class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = './index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyServer

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


