import socks
import socket
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#set socks5 proxy to use tor

socks.set_default_proxy(socks.SOCKS5, "185.132.177.153", 1080)
socket.socket = socks.socksocket
req = Request('https://sultandx.com', headers={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A105F Build/QP1A.190711.020)', })
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup('title')[0].get_text())
