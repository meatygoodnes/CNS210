import socket

#open ipv4 socket TCP
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The SQ_REUSEADDR flad tells the kernel to reuse a local socket in TIME_WAIT state without wating for its natural timeout to expire

mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds service to port 5555
mysocket.bind(('', 5555))

# Listens on the socket
mysocket.listen(0)

#Saves output data coming in of size 512
c, addr = mysocket.accept()
data = c.recv(512)

#if there is data print it out from the IP address and data it's self 
if data: 
    print("connection from: ", addr[0], ":", data)

# close socket
mysocket.close()
# nc localhost 5555 to connect
