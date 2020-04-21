#banner grabbing

import socket
import re

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("www.neverssl.com", 80))

http_get = b"GET / HTTP/1.1\nHost: www.neverssl.com\n\n" 
data = ''
try:
    mysocket.sendall(http_get)
    #data = mysocket.recvfrom(1024)
    data = mysocket.recvfrom(4096)
except socket.error:
    print("Socket error", socket.errno)
finally:
    mysocket.close()

strdata = data[0].decode("wtf-8")
headers = strdata.splitlines()
for s in headers:
    #if re.search('Server:' s):
        #s = s.replace(Server: ", "")
    print(s)
