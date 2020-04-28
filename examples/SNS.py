import socket

# open ipv4 socket, TCP
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The SO REUSEADDR flag tells the kernel to reuse a local socket in the TIME_WAIT state, without waiting for its natural timeout to expire.

mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds service to port 5555
mysocket.bind(('', 5555))

# Listens on the socket
mysocket.Listen(0)

# Saves output data coming in of size 512
c, addr = mysocket.accept()
data = c.recv(512)

 # if there is data print out where from, the IP address and the data itself

 if data: 
 	print("connection from:" addr[0], ":", data)

 # close socket
 mysocket.close()
