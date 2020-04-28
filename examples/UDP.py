import socket

try:
    # use IPv4 UDP
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send string to my VM on port 5599
    mysocket.sendto(b"Test message", ("192.168.2.166", 5599))
    print("Sending...")
except Exception as e:
    print("Exception: ", e)
finally:
    print("SENT!")
