import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import os

# ----------------------

# tworzy ścieżkę do folderu użytkownika
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
PORT = 8010
os.chdir(desktop)

handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()
print(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('127.0.0.1', 80))
IP = "http://" + '192.168.100.229' + ":" + str(PORT)
link = IP

print(s.getsockname())

url = pyqrcode.create(link)

url.svg('myqr.svg', scale=8)
webbrowser.open('myqr.svg')


with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"serving at port: {PORT}")
    print(f"type this on your browser: {IP}")
    print("or user the qrcode")
    httpd.serve_forever()


