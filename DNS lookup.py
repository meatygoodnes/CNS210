import socket

print("DNS lookup by IP address:", socket.gethostbyaddr("8.8.8.8"))

#loook up IP via host name server:
print("\n")
print("DNS loookup by name:", socket.gethostbyname("yahoo.com"))

#hardcoded from /etc/hosts, this will NOT work on your machine unless you add: 
print("\n")
print("DNS loookup by name", socket.gethostbyname("ctf.carhackingvillage.com"))

#This lookup includes all IP address responses instead of just one
print("\n")
print("DNS lookup with getaddrinfo:", socket.getaddrinfo("amazon.com", 53))

#this is to look up the fully qualified domain name
print("\n")
print("FQDN lookup:", socket.getfqdn("google.com"))