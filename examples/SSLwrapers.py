import ssl
import socket

# connect on IPv4 TCP

s = socket.socket.(socket.AF_INET, socket.SOCK_STREAM)

# use SSL wrapper
ssock = ssl.wrap_socket(s)

try:
    # Attempt to connect to Google on HTTPS
    ssock.connect(("www.google.com", 443))
    print(ssock.cipher())
except:
    print("error")

try:
    # Issue GET request
    ssock.write(b"GET / \r\n")
except Exception as e:
    print("write error: ", e)

# Save data
data = bytearray()
try:
    data = ssock.read()
except Exception as e:
    print("read error: ", e)

# print data
print(data.decode("utf-8"))
