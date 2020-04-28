import socket

# create an INET (IPv4) streaming socket (TCP)
mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now connecting to my own system on port 5555
mysocket.connect(('localhost', 5555))

# Set msg to be a byte str
msg=b"hi, sending data over a socket \n"

#attempt to send msg to socket
try:
    mysocket.sendall(msg)
except mysocket.errna as e:
    print("Socket error ", e)
finally:
    #close socket when done
    mysocket.close()
